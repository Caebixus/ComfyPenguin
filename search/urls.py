from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.searchpage, name='searchpage'),
    path('filter', views.filter, name='filter'),
    path('filter-mens-tops', views.filter_mens_tops, name='filter_mens_tops'),
    path('mens-tops', views.search_mens_tops, name='search_mens_tops'),
    path('filter-womens-tops', views.filter_womens_tops, name='filter_womens_tops'),
    path('womens-tops', views.search_womens_tops, name='search_womens_tops'),
]
