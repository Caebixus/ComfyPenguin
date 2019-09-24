from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='interesting-facts'),
    path('Why-size-chart-doesnt-work', views.clanek1, name='clanek1'),
    path('where-to-buy-hoodies-online-which-will-fit', views.clanek2, name='clanek2'),
    path('dress-size-calculator', views.clanek3, name='clanek3'),
    path('find-comfy-clothes-online', views.clanek4, name='clanek4'),
]
