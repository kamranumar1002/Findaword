from django.urls import path, include
from dictionaryapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    
]
