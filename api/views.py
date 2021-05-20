# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .serializers import SearchSerializer, BaseHadith, HadithSerializer, BaseHadithSerializer
# from core.engine.Engine import Engine
# from core.data.query_bundle import QueryBundle
# import core.data.hadith_data as hadith_data
#
# engine = Engine(index='hadith_15')
# engine.connect()
#
#
# def check_engine(fn):
#     def wrapper(*args, **kwargs):
#         if engine.get_engine_state():
#             return fn(*args, **kwargs)
#         return Response({"erro": "components is off"})
#
#     return wrapper
#
#
# @api_view(["GET", "POST"])
# @check_engine
# def simple_search(request):
#     if request.data:
#         serializer = SearchSerializer(data=request.data)
#         if serializer.is_valid():
#             result = engine.search(serializer.data)
#             # result = components.search(serializer.data['query'])
#             return Response(result)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response()
#
#
# # Collection
#
# @api_view(["GET", "POST"])
# def get_list_coll(request):
#     data = hadith_data.get_collections()
#     return Response(data)
#
#
# @api_view(["GET", "POST"])
# def get_coll(request, coll: str):
#     data = hadith_data.get_collection_by_name(coll)
#     return Response(data)
#
#
# @api_view(["GET", "POST"])
# def get_hadith_coll(request, coll: str):
#     data = engine.searcher.get_hadith_coll(coll)
#     return Response(data)
#
#
# # Chapter
#
# @api_view(["GET", "POST"])
# def get_chapter_coll(request, coll: str):
#     result = engine.searcher.get_hadith_coll(coll)
#     return Response(result)
#
#
# @api_view(["GET", "POST"])
# def get_hadith_chapter(request, coll: str, chapter_id: id):
#     result = engine.searcher.get_hadith_chapter(coll=coll, chapter=chapter_id)
#     return Response(result)
#
#
# # Section
# @api_view(["GET", "POST"])
# def get_hadith_section(request, coll: str, section_id: int):
#     result = engine.searcher.get_list_hadith_section(coll=coll, section_id=section_id)
#     return Response(result)
#
#
# # Hadith
#
# @api_view(["GET", "POST"])
# @check_engine
# def get_hadith(request):
#     # if id:
#     #     result = engine.searcher.get_hadith(id)
#     #     return Response(result)
#     # return Response()
#
#     if request.data:
#         serializer = HadithSerializer(data=request.data)
#         if serializer.is_valid():
#             data = serializer.data.copy()
#
#             result = engine.searcher.get_hadith(**data)
#             return Response(result)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # TODO implement this later
#     return Response()
#
#
# @api_view(["GET", "POST"])
# def get_random_hadith(request, coll=None):
#     if request.data:
#         serializer = BaseHadithSerializer(data=request.data)
#         if serializer.is_valid():
#             query_bundel = QueryBundle(data=serializer.get_data())
#             print(query_bundel.coll_name())
#             result = engine.searcher.get_random_hadith_new(query_bundel =query_bundel)
#             return Response(result)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     query_bundel = QueryBundle(data={})
#
#     result = engine.searcher.get_random_hadith_new(query_bundel)
#     return Response(result)
#
#
# #
# # @api_view(["GET", "POST"])
# # def get_random_coll(request, coll: str):
# #     result = engine.searcher.get_random_hadith(coll=coll)
# #     return Response(result)
#
#
# # Other
#
# @api_view(["GET"])
# def api_help(request):
#     return Response(
#         {
#             "Api version": "1.0",
#             "methodes": {
#                 "search": "localhost:8000/search",
#                 "devlopers": "localhost:8000/dev",
#             }
#         }
#     )
#
#
# @api_view(["GET"])
# def devlopers(request):
#     return Response({"API": "HADITH search components API",
#                      "API version": "1.0", "devloper": "berkane tarek"})
#
# #
# # @api_view(["GET", "POST"])
# # @check_engine
# # def get_hadith_serializer(request):
# #     # if id:
# #     #     result = engine.searcher.get_hadith(id)
# #     #     return Response(result)
# #     # return Response()
# #
# #     if request.data:
# #         serializer = HadithSerializer(data=request.data)
# #         # TODO valid can accept extra arguments
# #         if serializer.is_valid():
# #             result = engine.searcher.get_hadith_serializer(serializer)
# #             return Response(result)
# #
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     # TODO implement this later
# #     return Response()
# #
# #
# # @api_view(["GET", "POST"])
# # @check_engine
# # def get_hadith_by(request):
# #     if request.data:
# #         serializer = HadithListSerializer(data=request.data)
# #         # TODO valid can accept extra arguments
# #         if serializer.is_valid():
# #             result = engine.searcher.get_hadith_by(serializer)
# #             return Response(result)
# #
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #         # TODO implement this later
# #     return Response()

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BaseHadithSerializer, IdHadithSerializer,TextQuerySerializer
from core.engine.engine import Engine
from core.data.hadith_data import get_collections

# from core.data.query_bundle import QueryBundle
import core.data.hadith_data as hadith_data

engine = Engine(index='hadith_15')
# engine.connect()


def check_engine(fn):
    def wrapper(*args, **kwargs):
        if engine.get_engine_state():
            return fn(*args, **kwargs)
        return Response({"error": "engine is off"})

    return wrapper


@api_view(["GET", "POST"])
# @check_engine
def hadith(request):
    if request.data:
        # TODO add serializer
        serializer = IdHadithSerializer(data=request.data)
        if serializer.is_valid():
            result = engine.get_hadith_id_search_engine(serializer)
            print(result)
            return Response(result)

        else:
            return Response(serializer.errors)

    serializer = IdHadithSerializer()
    # todo : add help function to show all options
    return Response(serializer.help())

@api_view(["GET", "POST"])
# @check_engine
def get_random_hadith(request):
    if request.data:
        # TODO add serializer
        serializer = BaseHadithSerializer(data=request.data)
        if serializer.is_valid():
            result = engine.get_random_hadith_search_engine(serializer)
            return Response(result)

        else:
            return Response(serializer.errors)

    serializer = BaseHadithSerializer()
    # todo : add help function to show all options
    return Response(serializer.help())



@api_view(["GET", "POST"])
# @check_engine
def simple_search_api(request):
    if request.data:
        # TODO add serializer
        serializer = TextQuerySerializer(data=request.data)
        if serializer.is_valid():
            result = engine.simple_search_engine(serializer)
            return Response(result)

        else:
            return Response(serializer.errors)

    serializer = TextQuerySerializer()
    # todo : add help function to show all options
    return Response(serializer.help())



@api_view(["GET", "POST"])
# @check_engine
def get_coll(request):
    return Response(get_collections())