from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

ELASTICSEARCH_HOST = "nexxiscare-test.es.eu-west-1.aws.found.io"
ELASTICSEARCH_PORT = "443"
ELASTICSEARCH_USER = "nexxis_ingest"
ELASTICSEARCH_PASS = "xyWJUNXngL6QD2wG62vN"

def get_elastic_connection():
    try:
        es = Elasticsearch(
                [f'https://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}/'],
                http_auth=(f'{ELASTICSEARCH_USER}', f'{ELASTICSEARCH_PASS}'),
                timeout=60, verify_certs=True, use_ssl=True, retry_on_timeout=True, http_compress=True)
        print("Elastic initialized!")
        return es
    except Exception as error:
        print("elasticsearch is not reachable!")
        print(error)



def elastic_bulk_insert(es,index,bulk_insert):
    #response = bulk(es, bulk_insert, index=index, doc_type=doc_type, stats_only=False, chunk_size=200, raise_on_error=False) ##es 6.3
    response = bulk(es,
                bulk_insert,
                index=index,
                stats_only=False,
                chunk_size=200,
                raise_on_error=False)
