from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='interesting-facts'),
    path('Why-size-chart-doesnt-work', views.clanek1, name='clanek1'),
    path('Hoodie-size-chart-compare-to-size-search-engine', views.clanek2, name='clanek2'),
]
