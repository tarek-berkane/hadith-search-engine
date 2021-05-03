from elasticsearch import Elasticsearch
from elasticsearch.client import Elasticsearch as _es


def connect() -> _es:
    es = Elasticsearch([{"host": "localhost", "port": "9200"}])
    try:
        state = es.info()
        return es
    except Exception as e:
        es = None


