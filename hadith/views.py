from django.shortcuts import render
from core.engine.engine import Engine
from core.engine.components.helper import get_result

# Create your views here.

engine = Engine(index='hadith_15')
engine.start_engine()


def home(request):
    query = request.GET.get('hadith-search')

    items = []
    timing = None

    if query:
        # print(query)
        result = engine.searcher.simple_search(query)
        items = get_result(result)
        timing = result['took']

    return render(request, 'hadith/index.html', {"items": items, "time": timing})
