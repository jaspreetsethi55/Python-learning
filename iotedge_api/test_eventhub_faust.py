import faust
import ssl
from elastic_connect import get_elastic_connection, elastic_bulk_insert
import datetime
import time


SASL_USERNAME = "$ConnectionString"

EVENTHUB_NAMESPACE = "nexxissandboxtest"
SASL_PASSWORD = f"Endpoint=sb://nexxissandboxtest.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Ekd8fXNpN5BUguwmYhzP8r2e/M0vFAJPm+AEhAnzWhM="
topic_name = "nexxis_sandbox_eventhub"
#SASL_PASSWORD = "Endpoint=sb://iothub-ns-ne-nexxis-25158162-b0438eb667.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=3yfQEEDA48Lzj38DK4ySrucn8D9dO9RZuV8m2smbkF0="


'''
EVENTHUB_NAMESPACE = "nexxis-poc"
SASL_PASSWORD = f"Endpoint=sb://nexxis-poc.servicebus.windows.net/;SharedAccessKeyName=send-listen;SharedAccessKey=SLPsIX6i4y6+WvSwhDbyO4+VdTOv2IwgdVN8OXn1Y7g="
topic_name = "nexxis-eventhub"
'''

# Specify the Event Hubs Kafka endpoint and the SASL credentials
kafka_broker = f"{EVENTHUB_NAMESPACE}.servicebus.windows.net"
sasl_credentials = faust.SASLCredentials(
    username=SASL_USERNAME,
    password=SASL_PASSWORD,
    #ssl_context=create_ssl_context()
    mechanism=faust.types.auth.SASLMechanism.PLAIN,
    ssl_context=ssl.create_default_context()
)

# Create the Faust app
app = faust.App(
    'app',
    broker=f"kafka://nexxissandboxtest.servicebus.windows.net:9093",  # Use the Event Hubs Kafka endpoint
    broker_credentials=sasl_credentials,
    stream_wait_empty=False,
    store='memory://', stream_buffer_maxsize=100000
)

print(app)

BATCH_SIZE = 200
TIME_FRAME = 5

topic = app.topic(topic_name)
@app.agent(topic)
async def process(stream):
    try:
        print("Agent Started!")
        diagnostic_stream = stream.take(BATCH_SIZE, within=TIME_FRAME)
        async for diagnostic_chunk in diagnostic_stream:
            print("Batch length:",len(diagnostic_chunk))
            for diagnostic_state in diagnostic_chunk:
                print(type(diagnostic_state))
                print(diagnostic_state)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.main()
