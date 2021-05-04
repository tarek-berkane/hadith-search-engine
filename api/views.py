from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SearchSerializer
from engine.Engine import Engine

import api.hadith_data as hadith_data

engine = Engine(index='hadith_15')
engine.connect()


def check_engine(fn):
    def wrapper(*args, **kwargs):
        if engine.get_engine_state():
            return fn(*args, **kwargs)
        return Response({"erro": "components is off"})

    return wrapper


@api_view(["GET", "POST"])
@check_engine
def simple_search(request):
    if request.data:
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            result = engine.searcher.simple_search(serializer.data['query'])
            # result = components.search(serializer.data['query'])
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response()


# Collection

@api_view(["GET", "POST"])
def get_list_coll(request):
    data = hadith_data.get_collections()
    return Response(data)


@api_view(["GET", "POST"])
def get_coll(request, coll: str):
    data = hadith_data.get_collection_by_name(coll)
    return Response(data)


@api_view(["GET", "POST"])
def get_hadith_coll(request, coll: str):
    data = engine.searcher.get_hadith_coll(coll)
    return Response(data)


# Chapter

@api_view(["GET", "POST"])
def get_chapter_coll(request, coll: str):
    result = engine.searcher.get_hadith_coll(coll)
    return Response(result)


@api_view(["GET", "POST"])
def get_hadith_chapter(request, coll: str, chapter_id: id):
    result = engine.searcher.get_hadith_chapter(coll=coll, chapter=chapter_id)
    return Response(result)


# Section
@api_view(["GET", "POST"])
def get_hadith_section(request, coll: str, section_id: int):
    result = engine.searcher.get_list_hadith_section(coll=coll, section_id=section_id)
    return Response(result)


# Hadith

@api_view(["GET", "POST"])
@check_engine
def get_hadith(request, id=None):
    if id:
        result = engine.searcher.get_hadith(id)
        return Response(result)
    return Response()


@api_view(["GET", "POST"])
def get_random_hadith(request, coll=None):
    result = engine.searcher.get_random_hadith(coll=coll)
    return Response(result)

#
# @api_view(["GET", "POST"])
# def get_random_coll(request, coll: str):
#     result = engine.searcher.get_random_hadith(coll=coll)
#     return Response(result)


# Other

@api_view(["GET"])
def api_help(request):
    return Response(
        {
            "Api version": "1.0",
            "methodes": {
                "search": "localhost:8000/search",
                "devlopers": "localhost:8000/dev",
            }
        }
    )


@api_view(["GET"])
def devlopers(request):
    return Response({"API": "HADITH search components API",
                     "API version": "1.0", "devloper": "berkane tarek"})
