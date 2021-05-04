import elasticsearch.exceptions
from elasticsearch.client import Elasticsearch

from .elasticsearch_adapter.connecter import connect
from .elasticsearch_adapter import search_adapter
from .extractor import extract_hadith_item
from .text_analyzer import process_text_stemm, process_text_lemm


# es = connect()

# def test_connection():
#     try:
#         es.search()
#     except elasticsearch.exceptions.ConnectionError:
#         print("connection erroo")
#     except elasticsearch.exceptions.ConnectionTimeout:
#         print("connection time out ")


# def search_text(text: str):
#     return match_query(es=es, index='hadith_12', text=text)


def simple_search(es: Elasticsearch, index: str, text: str):
    return search_adapter.match_query(es=es, index=index, text=text)


class Searcher:
    def __init__(self, es: Elasticsearch, index: str):
        self._es = es
        self._index = index

    def simple_search(self, text: str):
        # todo add text analyzer
        processed_text = process_text_stemm(text)
        return search_adapter.match_query(es=self._es, index=self._index, text=processed_text)

    def get_hadith(self, id: int):
        result = search_adapter.search_hadith_by_id(es=self._es, index=self._index, id=id)
        if result:
            return extract_hadith_item(result)
        return {}

    def get_hadith_coll(self, coll):
        return search_adapter.get_hadith_coll(es=self._es, index=self._index, coll=coll)

    def get_hadith_chapter(self, coll: str, chapter: id):
        return search_adapter.get_hadith_chapter(es=self._es, index=self._index, coll=coll, chapter=chapter)

    def get_list_hadith_section(self, coll: str, section_id: int):
        return search_adapter.get_list_hadith_section(es=self._es, index=self._index, coll=coll, section_id=section_id)

    def get_random_hadith(self, coll=None):
        return search_adapter.get_random_hadith(es=self._es, index=self._index, coll=coll)
