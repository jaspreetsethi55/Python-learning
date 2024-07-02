import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
from elastic_connect import get_elastic_connection, elastic_bulk_insert
import datetime
import time

##The azure.eventhub.aio module is specifically designed to work with asynchronous programming using asyncio. If you want to use the EventHubConsumerClient without asyncio, you would typically use the synchronous version provided by the azure.eventhub module.

# Connection string to your Event Hub namespace
connection_string = "Endpoint=sb://iothub-ns-ne-nexxis-25158162-b0438eb667.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=3yfQEEDA48Lzj38DK4ySrucn8D9dO9RZuV8m2smbkF0=;EntityPath=ne-nexxis-sandbox-care-io"

##EventHub name - equivalent to kafka topic
eventhub_name = "ne-nexxis-sandbox-care-io"

# Event Hub consumer group to read from
consumer_group = "$Default"

## Blob storage connection string
storage_connection_str = "DefaultEndpointsProtocol=https;AccountName=nexxissandboxstorage001;AccountKey=7SG7mLn1JQvNfymczqH6tfr9uwm78vvn5kUw3PXu/wUI6bs6Gofw42BmUa7OQzFlAAb6GqtcSt/1+AStCVVS+g==;EndpointSuffix=core.windows.net"

## Blob storage container name
container_name = "nexxissandboxcontainerforeventhuboffset"

##This function will be called when consumer_client will receive any error
async def on_receiving_error(partition_context, error):
    # Put your code here. partition_context can be None in the on_error callback.

    ##partition_context is None: if error raised during the LB and error being the exception
    if partition_context:
        print("An exception: {} occurred during receiving from Partition: {}.".format(
            partition_context.partition_id,
            error
            ))
    else:
        print("An exception: {} occurred during the load balance process.".format(error))



async def batch_process_events(events):
    # put your code here

    bulk_insert = []
    for event_num,event in enumerate(events):
        event_json = event.body_as_json()
        print("Event Count: {}".format(event_num))
        bulk_insert.append(event_json)

    print(len(bulk_insert))
    if len(bulk_insert) > 0 :
        try:
            elastic_bulk_insert(es,'nexxis-eventhub-perf-diag',bulk_insert)
        except error as e:
            print("Error",e)
    #await asyncio.sleep(2)  # simulate something I/O bound

##This on_receiving_event function is called whenever a new event is received from the Event Hub.
async def on_receiving_batch_event(partition_context, events):
    ##'event' is the message payload

    ##body_as_json(encoding: str = 'UTF-8') -> Dict[str, Any]. Default encoding is UTF-8
    ##body_as_str(encoding: str = 'UTF-8') -> str. Default encoding is UTF-8

    print("Partition {}, Received count: {}".format(partition_context.partition_id, len(events)))
    try:
        await batch_process_events(events)
    except error as e:
        print("BATCH PROCESS ERROR",e)

    ##Updates the checkpoint using the given information for the offset, associated partition and consumer group in the chosen storage service.
    ##checkpoint: <xref:Dict>[<xref:str,Any>]
    ## Required: A dict containing checkpoint information:
    ##  fully_qualified_namespace (str): The fully qualified namespace that the Event Hub belongs to. The format is like ".servicebus.windows.net".
    ##  eventhub_name (str): The name of the specific Event Hub the checkpoint is associated with, relative to the Event Hubs namespace that contains it.
    ##  consumer_group (str): The name of the consumer group the checkpoint is associated with.
    ##  partition_id (str): The partition ID which the checkpoint is created for.
    ##  sequence_number (int): The sequence number of the EventData the new checkpoint will be associated with.
    ##  offset (str): The offset of the EventData the new checkpoint will be associated with.
    try:
        await partition_context.update_checkpoint()  # Or update_checkpoint every N events for better performance.
    except error as e:
        print("CHECKPOINT ERROR",e)

async def receive_events(consumer_client, checkpoint_store):

    async with consumer_client:
        # Receive messages from all partitions continuously
        await consumer_client.receive_batch(

            ##Required. The callback function for handling a received event.
            ##The callback takes two parameters: partition_context which contains partition context and event which is the received event.
            ##The callback function should be defined like: on_event(partition_context, event
            ##Type: Callable[['PartitionContext', 'EventData' | None], Awaitable[None]]
            on_event_batch = on_receiving_batch_event,

            ##The maximum interval in seconds that the event processor will wait before calling the callback.
            ##If no events are received within this interval, the on_event callback will be called with None.
            ##If this value is set to None or 0 (the default), the callback will not be called until an event is received
            ##Type: float
            max_wait_time = None,

            max_batch_size = 200,

            ##The number of events to prefetch from the service for processing. Default is 300
            ##Type: int
            prefetch = 300,

            ##If specified, the client will receive from this partition only. Otherwise the client will receive from all partitions.
            ##Type: str
            partition_id = None,

            ##Start receiving from this event position if there is no checkpoint data for a partition. Checkpoint data will be used if available.
            ##The value type can be str,int,datetime.datetime or dict with key:partition-ID and value: position for individual partitions or a single value for all partitions.
            ##Also supported are the values:
            ##         "-1" for receiving from the beginning of the stream
            ##         "@latest" for receiving only new events,
            ##         datetime.datetime.utcnow() means latest available event - after consumerclient is started
            ##Type: str, int, datetime or <xref:Dict>[<xref:str,Any>]
            #starting_position = datetime.datetime.utcnow(),
            starting_position = -1,


            ##The callback function that will be called when an error is raised during receiving after retry attempts are exhausted, or during the process of load-balancing
            ##The callback takes two parameters: partition_context which contains partition information(None if error raised during the LB)  and error being the exception.
            ##The callback should be defined like: on_error(partition_context, error).
            ##The on_error callback will also be called if an unhandled exception is raised during the on_event callback.
            ##Type: <xref:Callable>[[PartitionContext, Exception]
            on_error = on_receiving_error,
        )


if __name__ == "__main__":
    ##Making Blob connection for Eventhub checkpoint store
    checkpoint_store = BlobCheckpointStore.from_connection_string(
            storage_connection_str,
            container_name=container_name,
            #api_version="2023-08-03"
    )


    ##Making eventhub connection
    consumer_client = EventHubConsumerClient.from_connection_string(
            ##The connection string of an Event Hub -- Required.
            ##Type: str
            conn_str = connection_string,

            ##Receive events from the Event Hub for this consumer group -- Required.
            ##Type:str
            consumer_group  = consumer_group,

            ##The path of the specific Event Hub to connect the client to
            ##Type: str
            eventhub_name = eventhub_name,

            ##Whether to output network trace logs to the logger. Default is False.
            ##Type: bool
            logging_enable = True,

            ##The time in seconds to wait for a token to be authorized by the service.The default value is 60 seconds.If set to 0, no timeout will be enforced from the client.
            ##Type: float
            auth_timeout = 60,

            ##The total number of attempts to redo a failed operation when an error occurs. Default value is 3.
            ##Type: int
            retry_total = 3,

            ##A manager that stores the partition LB(load-balancing) and checkpoint data when receiving events.
            ##The checkpoint store will be used in both cases of receiving from all partitions or a single partition.
            ##In single partition case load-balancing does not apply.
            ##If checkpoint store is not provided, the checkpoint will be maintained internally in memory & the EventHubConsumerClient instance will receive events without LB
            ##Type: 'CheckpointStore'
            checkpoint_store = checkpoint_store,

            ##Timeout, in seconds, after which this client will close the underlying connection if there is no further activity.
            ##By default the value is None, meaning that the client will not shutdown due to inactivity unless initiated by the service.
            ##Type: float
            idle_timeout = None,

            ##Path to the custom CA_BUNDLE file of the SSL certificate which is used to authenticate the identity of the connection endpoint.
            ##Default is None in which case certifi.where() will be used
            ##Type: str
            connection_verify = None
            )

    es = get_elastic_connection()

    start = time.time()
    asyncio.run(receive_events(consumer_client, checkpoint_store))
    print(time.time() - start)
    '''
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(receive_events())
    except KeyboardInterrupt:
        print("Receiving has stopped.")
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
    '''

