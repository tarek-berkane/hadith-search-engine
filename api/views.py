from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SearchSerializer
from engine.engine import searcher, text_analyzer
from engine.engine.extractor import result_extractor


@api_view(['GET', "POST"])
def search_list(request):
    serializer = SearchSerializer(data=request.data)
    if request.data:
        if serializer.is_valid():
            # search using elasticSearch
            # TODO: add engine
            text = text_analyzer.process_text_stemm(serializer.data['query'])
            result = searcher.search_text(text=text)

            return Response(result_extractor(result))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response()


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
    return Response({"API": "HADITH search engine API",
                     "API version": "1.0", "devloper": "berkane tarek"})


@api_view(["GET"])
def search(request):
    pass
