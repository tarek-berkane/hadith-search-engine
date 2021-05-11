from elasticsearch.client import Elasticsearch

from .elasticsearch_adapter import search_adapter
from .extractor import extract_hadith_item
from .text_analyzer import process_text_stemm
import core.engine.components.elasticsearch_adapter.elasticsearch_models as template
from core.data.fields import QUERY, P_QUERY


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

    # def simple_search(self, text: str, **kwargs):
    #     # todo add text analyzer
    #     processed_text = process_text_stemm(text)
    #     return search_adapter.match_query(es=self._es, index=self._index, text=processed_text, **kwargs)
    #
    # def get_hadith(self, id: int, **kwargs):
    #     result = search_adapter.search_hadith_by_id(es=self._es, index=self._index, id=id, **kwargs)
    #     if result:
    #         return extract_hadith_item(result)
    #     return {}
    #
    # # def get_list_hadith(self,**kwargs):
    # #     result = search_adapter.
    # def get_hadith_coll(self, coll, **kwargs):
    #     return search_adapter.get_hadith_coll(es=self._es, index=self._index, coll=coll, **kwargs)
    #
    # def get_hadith_chapter(self, coll: str, chapter: id, **kwargs):
    #     return search_adapter.get_hadith_chapter(es=self._es, index=self._index, coll=coll, chapter=chapter, **kwargs)
    #
    # def get_list_hadith_section(self, coll: str, section_id: int, **kwargs):
    #     return search_adapter.get_list_hadith_section(es=self._es, index=self._index, coll=coll,
    #                                                   section_id=section_id, **kwargs)
    #
    # def get_random_hadith(self, coll=None, **kwargs):
    #     return search_adapter.get_random_hadith(es=self._es, index=self._index, coll=coll, **kwargs)
    #
    # def get_random_hadith_new(self, query_bundel, **kwargs):
    #     data = get_random_hadith_model_test(query_bundel, **kwargs)
    #
    #     return self._es.search(index=self._index, body=data)
    #
    # # new items
    # def get_hadith_new(self, hadith_number: int, coll_id: int = None,
    #                    coll: str = None, chapter_number: int = None,
    #                    section_number: int = None):
    #     data = get_hadith_model(
    #         hadith_number=hadith_number,
    #         coll_id=coll_id, coll=coll, chapter_number=chapter_number,
    #         section_number=section_number)
    #
    #     return self._es.search(index=self._index, body=data)
    #
    # def get_list_hadith(self, coll_id: int = None,
    #                     coll_name: str = None, chapter_id: int = None,
    #                     section_id: int = None):
    #     data = get_hadith_model(coll_id, coll_name, chapter_id, section_id)
    #     return self._es.search(index=self._index, body=data)
    #
    # def get_list_chapter(self, coll_id: int = None,
    #                      coll_name: str = None):
    #     # TODO: implement get_list_chapter
    #     raise NotImplemented()
    #
    # def get_list_section(self, coll_id: int = None,
    #                      coll_name: str = None):
    #     # TODO: implement get_list_section
    #     raise NotImplemented()
    #
    # # def get_list_coll(self):
    # #     return get_collections()
    # #
    # # def get_coll(self, coll_name: str):
    # #     return get_collection_by_name(coll_name)
    #
    # # def get_random_hadith_new(self, coll_id: int = None,
    # #                           coll: str = None, chapter_number: int = None,
    # #                           section_number: int = None):
    # #     data = get_random_hadith_model(coll_id, coll, chapter_number, section_number)
    # #
    # #     return self._es.search(index=self._index, body=data)
    #
    # def get_random_hadith_new(self,query_bundel):
    #     data = get_random_hadith_model_test(query_bundel)
    #
    #     return self._es.search(index=self._index, body=data)
    #
    # # search
    #
    # def simple_search(self, query: str):
    #     data = simple_serach_model(query)
    #
    #     return self._es.search(index=self._index, body=data)
    #
    # # ---------------------------------------------
    # # ---------------------------------------------
    # # ---------------------------------------------
    # # ---------------------------------------------
    # # ---------------------------------------------
    # # ---------------------------------------------
    # # ---------------------------------------------
    # # def get_hadith_serializer(self, hadithSeriaizer: HadithSerializer):
    # #     data = get_hadith_model_serializer(hadithSeriaizer)
    # #
    # #     return self._es.search(index=self._index, body=data)
    # #
    # # def get_hadith_by(self, hadithListSerializer: HadithListSerializer):
    # #     data = get_hadith_by(hadithListSerializer)
    # #
    # #     return self._es.search(index=self._index, body=data)

    # search for text
    def simple_search(self, serializer, **kwargs):
        # todo add text analyzer
        # processed_text = process_text_stemm(serializer.get_data()[QUERY])

        # extra_option = {P_QUERY: processed_text}
        query_body = template.simple_search_template(serializer, **kwargs)

        return self._es.search(index=self._index, body=query_body)


    # hadith section
    def get_random_hadith_search(self, serializer):
        query_body = template.get_random_hadith_template(serializer)

        return self._es.search(index=self._index, body=query_body)

    def get_hadith_id_search(self, serializer):
        query_body = template.get_hadith_id_template(serializer)

        return self._es.search(index=self._index, body=query_body)
