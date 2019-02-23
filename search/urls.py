from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.searchpage, name='searchpage'),
    path('filter', views.filter, name='filter'),
]
