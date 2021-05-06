from django.shortcuts import render
from engine.Engine import Engine
from engine.components.helper import get_result
# Create your views here.

engine = Engine(index='hadith_15')
engine.connect()


def home(request):
    query = request.GET.get('hadith-search')

    items = []

    if query:
        # print(query)
        result = engine.searcher.simple_search(query)
        items = get_result(result)
        timing = result['took']


    return render(request, 'hadith/index.html', {"items": items,"time":timing})

