import asyncio

from azure.eventhub.aio import EventHubProducerClient  # The package name suffixed with ".aio" for async
from azure.eventhub import EventData

connection_str = "Endpoint=sb://nexxissandboxtest.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Ekd8fXNpN5BUguwmYhzP8r2e/M0vFAJPm+AEhAnzWhM="
#f"Endpoint=sb://nexxissandboxtest.servicebus.windows.net/;SharedAccessKeyName=owner;SharedAccessKey=4QObcpzJkfS2fVXQ06zethv1viK2mOZcf+AEhGOLubc=;EntityPath=nexxis_sandbox_eventhub"


eventhub_name = "nexxis_sandbox_eventhub"


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a credential that has correct role assigned to access
    # event hubs namespace and the event hub name.

    producer = EventHubProducerClient.from_connection_string(
    connection_str, eventhub_name=eventhub_name)
    
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData("First event "))
        event_data_batch.add(EventData("Second event"))
        event_data_batch.add(EventData("Third event"))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

        # Close credential when no longer needed.
        #await credential.close()

asyncio.run(run())
