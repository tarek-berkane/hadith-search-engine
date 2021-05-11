# from api.serializers import HadithSerializer, HadithListSerializer

import core.data.fields as fields
# from core.data.query_bundle import QueryBundle
import core.data.fields as fd


# Exceptions


class NotConfiguredProperlyError(Exception):
    def __init__(self, msg, reason):
        self.msg = msg
        self.reason = reason

    def __str__(self):
        return self.msg


# Helper functions

def get_match_model(hadith_number: int = None, coll_id: int = None,
                    coll: str = None, chapter_number: int = None,
                    section_number: int = None, **kwargs) -> dict:
    data = []

    if fields.HADITH_NUMBER:
        data.append({"match": {fd.HADITH_NUMBER: {"query": hadith_number}}})
        # data.append({'hadith_number': hadith_id})

    if coll:
        data.append({"match": {fd.COLLECTION: {"query": coll}}})
        # data.append({'coll': coll_name})

    if section_number:
        data.append({"match": {fd.SECTION_NUMBER: {"query": section_number}}})
        # data.append({'section_number': section_id})

    if chapter_number:
        data.append({"match": {fd.CHAPTER_NUMBER: {"query": chapter_number}}})
        # data.append({'chapter_number': chapter_id})

    return data


def get_hadith_model(hadith_number: int, coll_id: int = None,
                     coll: str = None, chapter_number: int = None,
                     section_number: int = None) -> dict:
    if coll_id and coll:
        raise NotConfiguredProperlyError(
            "Both coll_id and coll_name options cannot be used at the same time",
            "coll_id != None and coll_name != None")

    data = {"query": {
        "bool": {
            "must": [
            ]

        }
    },
    }

    # TODO add coll_id here and in mapping
    # this need to reindex the hole documents in elasticsearch
    if hadith_number:
        data['query']['bool']['must'].append(
            {"match": {"hadith_number": hadith_number}}, )
        # data['hadith_number'] = hadith_number

    if coll:
        data['query']['bool']['must'].append({"match": {"coll": coll}}, )
        # data['coll'] = coll

    if section_number:
        data['query']['bool']['must'].append(
            {"match": {"section_number": section_number}}, )
        # data["section_number"] = section_number

    if chapter_number:
        data['query']['bool']['must'].append(
            {"match": {"chapter_number": chapter_number}}, )
        # data["chapter_number"] = chapter_number

    return data


def simple_serach_model(query: str):
    data = {
        "query": {
            "simple_query_string": {
                "fields": ["matn_p", "isnad_p"],
                "query": query,
                "flags": "OR|AND|PREFIX"
            }
        }
    }

    return data


def get_random_hadith_model(**kwargs):
    data = {"size": 10,
            "query": {
                "function_score": {
                    "query": {"bool": {
                        "must": get_match_model(**kwargs)
                    }},
                    "random_score": {}
                }
            }}

    return data

    # ---------------------------------------------
    # ---------------------------------------------
    # ---------------------------------------------
    # ---------------------------------------------
    # ---------------------------------------------
    # ---------------------------------------------
    # ---------------------------------------------


# def get_hadith_model_serializer(hadithSeriaizer: HadithSerializer) -> dict:
#     query_items = hadithSeriaizer.data
#
#     # if hadithSeriaizer.data['coll_id'] and hadithSeriaizer.data['coll']:
#     #     raise NotConfiguredProperlyError(
#     #         "Both coll_id and coll_name options cannot be used at the same time",
#     #         "coll_id != None and coll_name != None")
#
#     data = {"query": {
#         "bool": {
#             "must": [
#                 # {"match": {"coll": coll}},
#                 # {"match": {"chapter_number": section_id}},
#             ]
#
#         }
#     },
#     }
#
#     # TODO add coll_id here and in mapping
#     # this need to reindex the hole documents in elasticsearch
#     if query_items["hadith_number"]:
#         data['query']['bool']['must'].append(
#             {"match": {"hadith_number": query_items["hadith_number"]}}, )
#         # data['hadith_number'] = hadith_number
#
#     if query_items['coll']:
#         data['query']['bool']['must'].append(
#             {"match": {"coll": query_items["coll"]}}, )
#         # data['coll'] = coll
#
#     # if query_items['section_number']:
#     #     data['query']['bool']['must'].append({"match": {"section_number": query_items['section_number']}}, )
#     #     # data["section_number"] = section_number
#     #
#     # if query_items['chapter_number']:
#     #     data['query']['bool']['must'].append({"match": {"chapter_number": query_items['chapter_number']}}, )
#     #     # data["chapter_number"] = chapter_number
#
#     return data


# def get_hadith_by(hadithListSerializer: HadithListSerializer):
#     query_items = hadithListSerializer.data
#
#     data = {"query": {
#         "bool": {"must": []}
#     },
#     }
#
#     if query_items['section_number']:
#         data['query']['bool']['must'].append(
#             {"match": {"section_number": query_items['section_number']}}, )
#
#     if query_items['chapter_number']:
#         data['query']['bool']['must'].append(
#             {"match": {"chapter_number": query_items['chapter_number']}}, )
#
#     return data


def get_match_model_serializer(serializer, **kwargs) -> dict:
    query_data = serializer.get_data()
    data = []

    if hadith_number := query_data.get(fd.HADITH_NUMBER):
        print("here")
        data.append({"match": {fd.HADITH_NUMBER: {"query": hadith_number}}})

    if coll_name := query_data.get(fd.COLLECTION):
        data.append({"match": {fd.COLLECTION: {"query": coll_name}}})

    if section_number := query_data.get(fd.SECTION_NUMBER):
        data.append({"match": {fd.SECTION_NUMBER: {"query": section_number}}})

    if chapter_number := query_data.get(fd.CHAPTER_NUMBER):
        data.append({"match": {fd.CHAPTER_NUMBER: {"query": chapter_number}}})

    return data


# def get_match_id_serializer(serializer,**kwargs):
#     query_data = get_match_model_serializer(serializer,**kwargs)
#     data = []


def get_random_hadith_template(serializer, **kwargs):
    data = {"size": 10,
            "query": {
                "function_score": {
                    "query": {"bool": {
                        "must": get_match_model_serializer(serializer, **kwargs)
                    }},
                    "random_score": {}
                }
            }}

    return data


def get_hadith_id_template(serializer, **kwargs):
    query_data = serializer.get_data()

    data = {
        "query": {
            "bool": {"must": get_match_model_serializer(serializer, **kwargs)}
        },
    }

    return data


def simple_search_template(serializer, **kwargs):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "simple_query_string": {
                            "fields": ["matn_p", "isnad_p"],
                            "query": kwargs.get(fd.P_QUERY),
                            "flags": "OR|AND|PREFIX"
                        }
                    },
                    # {"function_score": {
                    #     "query": {
                    #         "match_phrase": {
                    #             "isnad_p": kwargs.get(fd.P_QUERY)
                    #         }
                    #     },
                    #     "boost": "5",
                    #     "random_score": {},
                    #     "boost_mode": "multiply"
                    # }},
                    # {"function_score": {
                    #     "query": {
                    #         "match_phrase": {
                    #             "matn_p": kwargs.get(fd.P_QUERY)
                    #         }
                    #     },
                    #     "boost": "5",
                    #     "random_score": {},
                    #     "boost_mode": "multiply"
                    # }}
                ],
                # "should": [
                #     {
                #         "intervals": {
                #             "isnad_p": {
                #                 "all_of": {
                #                     "ordered": True,
                #                     "intervals": [
                #                         {
                #                             "match": {
                #                                 "query": kwargs.get(fd.P_QUERY),
                #                                 "max_gaps": 1,
                #                                 "ordered": True,
                #
                #                             }
                #                         },
                #                         # {
                #                         #     "any_of": {
                #                         #         "intervals": [
                #                         #             {"match": {"query": text}},
                #                         #             {"match": {"query": text}}
                #                         #         ]
                #                         #     }
                #                         # }
                #                     ]
                #                 }
                #             }
                #         }
                #     }
                # ]
            }
        }
    }
    extra_data = get_match_model_serializer(serializer, **kwargs)
    for item in extra_data:
        query['query']['bool']['must'].append(item)

    return query
