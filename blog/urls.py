from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='interesting-facts'),
    path('Why-size-chart-doesnt-work', views.clanek1, name='clanek1'),
]
