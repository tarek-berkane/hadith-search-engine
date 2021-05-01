from elasticsearch import Elasticsearch
from elasticsearch.client import Elasticsearch as _es



def boolean_query(es: _es, index: str):
    es.search()


def boosting_query():
    pass


def match_query(es: _es, index: str, text: str):
    query = {
        "query": {
            "match": {
                "maten": {
                    "query": text
                }
            }
        }
    }
    return es.search(index=index, body=query)

