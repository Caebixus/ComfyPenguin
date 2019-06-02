from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('about', views.aboutus, name='aboutus'),
    path('how-to-measure', views.how_to_measure, name='how_to_measure'),
    path('how-to-measure-sweatshirt', views.how_to_measure_sweatshirt, name='how_to_measure_sweatshirt'),
    path('how-to-measure-jumper', views.how_to_measure_jumper, name='how_to_measure_jumper'),
    path('how-to-measure-hoodie', views.how_to_measure_hoodie, name='how_to_measure_hoodie'),
    path('search/', include('search.urls'), name='search'),
    path('clothes/', include('clothes.urls'), name='clothes'),
    path('Interesting-facts/', include('blog.urls'), name='blog'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
