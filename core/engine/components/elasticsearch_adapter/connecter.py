from elasticsearch import Elasticsearch
from elasticsearch.client import Elasticsearch as _es


def connect() -> _es:
    return Elasticsearch([{"host": "localhost", "port": "9200"}])

