import elasticsearch.exceptions
from elasticsearch.client import Elasticsearch

from .elasticsearch_adapter.connecter import connect
from .elasticsearch_adapter.search_adapter import match_query
from .text_analyzer import process_text_stemm, process_text_lemm

es = connect()

def test_connection():
    try:
        es.search()
    except elasticsearch.exceptions.ConnectionError:
        print("connection erroo")
    except elasticsearch.exceptions.ConnectionTimeout:
        print("connection time out ")

def search_text(text: str):
    return match_query(es=es, index='hadith_12', text=text)


def simple_search(es: Elasticsearch, index: str, text: str):
    return match_query(es=es, index=index, text=text)


