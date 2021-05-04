from django.urls import path
from . import views

urlpatterns = [
    # path('api/', views.api_help),
    path('dev/', views.devlopers),
    path('search/', views.simple_search),
    path('hadith/<int:id>', views.get_hadith),
    path('hadith/random', views.get_random_hadith),
    path('coll/', views.get_list_coll),
    path('coll/<str:coll>', views.get_coll),
    path('coll/<str:coll>/hadith', views.get_hadith_coll),
    path('coll/<str:coll>/hadith/random', views.get_random_hadith),
    path('coll/<str:coll>/chapter/<int:chapter_id>/hadith', views.get_hadith_chapter),
    path('coll/<str:coll>/section/<int:section_id>/hadith', views.get_hadith_section),
    # path('snippets/<int:pk>/', views.snippet_detail),

    # path('snippets/<int:pk>/', views.snippet_detail),
]
