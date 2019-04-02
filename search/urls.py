from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.searchpage, name='searchpage'),
    path('filter', views.filter, name='filter'),
    path('filter-mens-tops', views.filter_mens_tops, name='filter_mens_tops'),
    path('mens-tops', views.search_mens_tops, name='search_mens_tops'),
    path('filter-womens-tops', views.filter_womens_tops, name='filter_womens_tops'),
    path('search_womens_tops_sweatshirts', views.search_womens_tops_sweatshirts, name='search_womens_tops_sweatshirts'),
    path('search_womens_tops_hoodies', views.search_womens_tops_hoodies, name='search_womens_tops_hoodies'),
    path('search_womens_tops_jumpers', views.search_womens_tops_jumpers, name='search_womens_tops_jumpers'),
    path('search_mens_tops_sweatshirts', views.search_mens_tops_sweatshirts, name='search_mens_tops_sweatshirts'),
    path('search_mens_tops_hoodies', views.search_mens_tops_hoodies, name='search_mens_tops_hoodies'),
    path('search_mens_tops_jumpers', views.search_mens_tops_jumpers, name='search_mens_tops_jumpers'),
    path('womens-tops', views.search_womens_tops, name='search_womens_tops'),
]
