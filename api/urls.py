from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_help),
    path('dev/', views.devlopers),
    path('search/', views.simple_search),
    # path('snippets/<int:pk>/', views.snippet_detail),
]