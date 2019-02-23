from django.urls import path, include
from . import views

urlpatterns = [
    path('interesting-facts', views.blog, name='interesting-facts'),
]
