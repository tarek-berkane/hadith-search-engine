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


def search_hadith_by_id(es: Elasticsearch, index: str, id: int):
    return es.get(index=index, id=id)


def get_hadith_chap(es: Elasticsearch, index: str, text: str):
    return es.search(index=index, body=
    {"query": {
        "match": {
            "chapter_arabic": {"query": text}
        }
    }})


def get_hadith_coll(es: Elasticsearch, index: str, coll: str):
    return es.search(index=index, body={
        "size": 20,
        "query": {
            "match": {
                "coll": coll
            },
        },
        # TODO sort search by id
        "sort": [
            {"hadith_number": {"order": "asc"}}
        ]
    })


def get_hadith_chapter(es: Elasticsearch, index: str, coll: str, chapter: id):
    return es.search(index=index, body={
        "query": {
            "bool": {
                "must": [
                    {"match": {"coll": coll}},
                    {"match": {"chapter_number": chapter}},
                ]

            }
        },
    })


def get_list_hadith_section(es: Elasticsearch, index: str, coll: str, section_id: id):
    return es.search(index=index, body={"query": {
        "bool": {
            "must": [
                {"match": {"coll": coll}},
                {"match": {"chapter_number": section_id}},
            ]

        }
    },
    })


def get_random_hadith(es: Elasticsearch, index: str, coll: str):
    body = {"size": 10,
            "query": {
                "function_score": {
                    "query": {"match_all": {}},
                    "random_score": {}
                }
            }}

    if coll:
        body['query']['function_score']['query'] = {"match": {"coll": coll}}

    return es.search(index=index, body=body)
