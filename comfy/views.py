from django.shortcuts import render
from clothes.models import Product_Clothes_Tops
from comfy.choices import GENDER_CHOICES, CATEGORY_CHOICES, CONTINENT_CHOICES

def homepage(request):
    listing = Product_Clothes_Tops.objects.all()
    my_total = Product_Clothes_Tops.objects.count()

    # counting Mans clothes
    my_total_men = Product_Clothes_Tops.objects.filter(item_gender__iexact="Male")
    my_total_men_count = my_total_men.count()

    # counting Mans clothes
    my_total_woman = Product_Clothes_Tops.objects.filter(item_gender__iexact="Female")
    my_total_woman_count = my_total_woman.count()

    # counting Mans clothes
    my_total_kid = Product_Clothes_Tops.objects.filter(item_gender__iexact="Kids")
    my_total_kid_count = my_total_kid.count()

    # counting Mans clothes
    my_total_uni = Product_Clothes_Tops.objects.filter(item_gender__iexact="Unisex")
    my_total_uni_count = my_total_uni.count()

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': listing,
        'my_total': my_total,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }

    return render(request, 'homepage.html', context)

def search(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
    my_total = Product_Clothes_Tops.objects.count()
    queryset_list = Product_Clothes_Tops.objects.order_by('?')

    #Width
    if 'width' in request.GET:
        widths = request.GET['width']
        widthx = int(widths) + 2
        if widths:
            queryset_list = queryset_list.filter(item_width__range=(widths, widthx))

    #Height
    if 'height' in request.GET:
        heights = request.GET['height']
        heightx = int(heights) + 2
        if heights:
            queryset_list = queryset_list.filter(item_height__range=(heights, heightx))

    #Type
    if 'Type' in request.GET:
        types = request.GET['Type']
        if types:
            queryset_list = queryset_list.filter(item_category__iexact=types)

    #Country
    if 'Continent' in request.GET:
        countries = request.GET['Continent']
        if countries:
            queryset_list = queryset_list.filter(item_continent__iexact=countries)

    queryset_list = queryset_list.filter(item_gender__iexact=Female)

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
    }
    return render(request, 'search.html', context)

def sitemap(request):
    return render(request, 'sitemap.xml')

def aboutus(request):
    return render(request, 'aboutus.html')

def how_to_measure(request):
    return render(request, 'how-to-measure.html')
