from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('Change-password', views.change_password, name='Change-password'),
    path('My-comfy-clothes/<int:myclothes_id>', views.My_comfy_clothes, name='My-comfy-clothes'),
    path('Delete-comfy-clothes/<int:myclothes_id>', views.Delete_comfy_clothes, name='Delete-comfy-clothes'),
    path('Create-comfy-clothes', views.Create_comfy_clothes, name='Create-comfy-clothes'),
    path('Edit-profile', views.edit_profile, name='Edit-profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
