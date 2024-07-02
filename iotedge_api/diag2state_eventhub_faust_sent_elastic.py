import faust
from os import environ
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from nexxis import device_by_name, extract_diagnostic_data
from state import State
import health_monitor as hm
import ssl
from logger import logger_init

log = logger_init()
hm.initialize_logger(log)
APP_LIVE_TIME = 111

try:
    ENV_NAME = environ["ENV_NAME"]
    KAFKA_HOST = environ["KAFKA_HOST"]
    KAFKA_HOST_LIST = KAFKA_HOST.split(';')
    ELASTICSEARCH_HOST = environ["ELASTICSEARCH_HOST"]
    ELASTICSEARCH_USER = environ["ELASTICSEARCH_USER"]
    ELASTICSEARCH_PASS = environ["ELASTICSEARCH_PASS"]
    ELASTICSEARCH_PORT = environ["ELASTICSEARCH_PORT"]
except KeyError as error:
    log.error("Not all environment variables are set! ".format(error))

SASL_USERNAME = "$ConnectionString"

EVENTHUB_NAMESPACE = "nexxissandboxtest"
SASL_PASSWORD = f"Endpoint=sb://nexxissandboxtest.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Ekd8fXNpN5BUguwmYhzP8r2e/M0vFAJPm+AEhAnzWhM="
topic_name = "nexxis_sandbox_eventhub"


# Specify the Event Hubs Kafka endpoint and the SASL credentials
kafka_broker = f"{EVENTHUB_NAMESPACE}.servicebus.windows.net"
sasl_credentials = faust.SASLCredentials(
    username=SASL_USERNAME,
    password=SASL_PASSWORD,
    #ssl_context=create_ssl_context()
    mechanism=faust.types.auth.SASLMechanism.PLAIN,
    ssl_context=ssl.create_default_context()
)


app = faust.App(f'nexxis-device-state-extract-{ENV_NAME}',
                broker= ['kafka://nexxissandboxtest.servicebus.windows.net:9093'],
                broker_credentials=sasl_credentials,
                stream_wait_empty=False,
                store='memory://', stream_buffer_maxsize=100000, loghandlers=log.handlers)

try:
    es = Elasticsearch([f'https://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}/'],
                       http_auth=(f'{ELASTICSEARCH_USER}', f'{ELASTICSEARCH_PASS}'),
                       timeout=60, verify_certs=True, retry_on_timeout=True, http_compress=True)
except Exception as error:
    log.error("Elastic Search is not reachable!")
    log.error(error)


# Kafka topics on which the incoming diagnostic events are expected ...
DIAGNOSTICS_TOPIC = app.topic(topic_name)

# Elastic indexes for the timestamped state and the state of time documents ...
STATE_INDEX = f"nexxis-device-state-{ENV_NAME}"
BATCH_SIZE = 200
TIME_FRAME = 5

@app.agent(DIAGNOSTICS_TOPIC)
async def process(stream):
    try:
        log.info("Agent Started!")
        diagnostics_stream = stream.take(BATCH_SIZE, within=TIME_FRAME)
        async for diagnostic_chunk in diagnostics_stream:
            bulk_insert = []
            print("Event Count: {}".format(len(diagnostic_chunk)))
            for diagnostic_state in diagnostic_chunk:
                bulk_insert.append(diagnostic_state)
            print(len(bulk_insert))
            if len(bulk_insert) > 0:
                try:
                    bulk(es, bulk_insert, index='nexxis-eventhub-perf-diag', stats_only=False, chunk_size=200, raise_on_error=False)
                except error as e:
                    print("Error",e)
    except Exception as err:
        log.error("Exception {} caught processing.".format(err))


@app.timer(interval=11)
async def live_file_writer():
    try:
        hm.write_live_file()
    except Exception as ex:
        log.error("Liveness Heartbeat Exception {} caught processing.".format(ex))


@app.timer(interval=13)
async def state_file_writer():
    try:
        hm.write_state_file()
    except Exception as ex:
        log.error("State Heartbeat Exception {} caught processing.".format(ex))


# live api with faust's default http server
@app.page("/status/live")
async def check_liveness(self, request):
    # time difference between last updated livetstamp and current time
    # should not be more then 30 seconds
    try:
        res = hm.check_liveness("diag2state", app_live_time=APP_LIVE_TIME)
        return self.json(res[0], status=res[1])
    except Exception as ex:
        log.error("Liveness probe Exception {} caught processing.".format(ex))


# ready api page to check readiness
@app.page('/status/ready')
async def check_readiness(self, request):
    try:
        res = hm.check_ready_state("diag2state", app_live_time=APP_LIVE_TIME)
        return self.json(res[0], status=res[1])
    except Exception as ex:
        log.error("Readiness probe Exception {} caught processing.".format(ex))


# health api will check app and other components.
@app.page('/status/health')
async def check_health(self, request):
    # time difference between last updated livetstamp and current time
    # should not be more then 30 seconds
    try:
        res = hm.check_app_health("diag2state", app_live_time=APP_LIVE_TIME)
        return self.json(res[0], status=res[1])
    except Exception as ex:
        log.error("Health check Exception {} caught processing.".format(ex))

