from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('search/', include('search.urls'), name='search'),
    path('clothes/', include('clothes.urls'), name='clothes'),
    path('blog/', include('blog.urls'), name='blog'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
