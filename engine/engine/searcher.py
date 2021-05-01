from .elasticsearch_adapter.connecter import connect
from .elasticsearch_adapter.search_adapter import match_query
from .text_analyzer import process_text_stemm, process_text_lemm

es = connect()


def search_text(text: str):
    return match_query(es=es, index='hadith_12', text=text)
