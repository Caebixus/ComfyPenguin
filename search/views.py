from django.shortcuts import render
from clothes.models import Product_Clothes_Tops
from comfy.choices import GENDER_CHOICES, CATEGORY_CHOICES, CONTINENT_CHOICES, CATEGORY_CHOICES_MALE, CATEGORY_CHOICES_FEMALE
from comfy.views import search
from django.core.paginator import Paginator

# Create your views here.

def searchpage(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search.html', context)

#
#
#

def filter(request):

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
    }

    return render(request, 'filter.html', context)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

def search_mens_tops(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
    queryset_list = queryset_list.filter(item_gender__iexact='Male')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_MALE': CATEGORY_CHOICES_MALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-mens-tops.html', context)

def filter_mens_tops(request):

    context = {
        'CATEGORY_CHOICES_MALE': CATEGORY_CHOICES_MALE,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
    }

    return render(request, 'filter-mens-tops.html', context)

def search_mens_tops_sweatshirts(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
            queryset_list = queryset_list.filter(item_category__iexact='sweatshirt')
    #Country
    if 'Continent' in request.GET:
        countries = request.GET['Continent']
        if countries:
            queryset_list = queryset_list.filter(item_continent__iexact=countries)
    queryset_list = queryset_list.filter(item_gender__iexact='Male', item_category__iexact='sweatshirt')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_MALE': CATEGORY_CHOICES_MALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-mens-tops.html', context)

def search_mens_tops_hoodies(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
            queryset_list = queryset_list.filter(item_category__iexact='Hoodies')
    #Country
    if 'Continent' in request.GET:
        countries = request.GET['Continent']
        if countries:
            queryset_list = queryset_list.filter(item_continent__iexact=countries)
    queryset_list = queryset_list.filter(item_gender__iexact='Male', item_category__iexact='Hoodies')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_MALE': CATEGORY_CHOICES_MALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-mens-tops.html', context)

def search_mens_tops_jumpers(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
            queryset_list = queryset_list.filter(item_category__iexact='Jumper')
    #Country
    if 'Continent' in request.GET:
        countries = request.GET['Continent']
        if countries:
            queryset_list = queryset_list.filter(item_continent__iexact=countries)
    queryset_list = queryset_list.filter(item_gender__iexact='Male', item_category__iexact='Jumper')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_MALE': CATEGORY_CHOICES_MALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-mens-tops.html', context)

#
#
#

def search_womens_tops(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
    queryset_list = queryset_list.filter(item_gender__iexact='Female')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    my_total_searched_sweatshirts = queryset_list.filter(item_category__iexact='sweatshirt', item_gender__iexact='Female').count()
    my_total_searched_hoodies = queryset_list.filter(item_category__iexact='Hoodies', item_gender__iexact='Female').count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_FEMALE': CATEGORY_CHOICES_FEMALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_searched_sweatshirts': my_total_searched_sweatshirts,
        'my_total_searched_hoodies': my_total_searched_hoodies,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-womens-tops.html', context)

def search_womens_tops_sweatshirts(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
            queryset_list = queryset_list.filter(item_category__iexact='sweatshirt')
    #Country
    if 'Continent' in request.GET:
        countries = request.GET['Continent']
        if countries:
            queryset_list = queryset_list.filter(item_continent__iexact=countries)
    queryset_list = queryset_list.filter(item_gender__iexact='Female', item_category__iexact='sweatshirt')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_FEMALE': CATEGORY_CHOICES_FEMALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-womens-tops.html', context)

def search_womens_tops_hoodies(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
            queryset_list = queryset_list.filter(item_category__iexact='Hoodies')
    #Country
    if 'Continent' in request.GET:
        countries = request.GET['Continent']
        if countries:
            queryset_list = queryset_list.filter(item_continent__iexact=countries)
    queryset_list = queryset_list.filter(item_gender__iexact='Female', item_category__iexact='Hoodies')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_FEMALE': CATEGORY_CHOICES_FEMALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-womens-tops.html', context)

def search_womens_tops_jumpers(request):
    listing = Product_Clothes_Tops.objects.all()[:8]
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
            queryset_list = queryset_list.filter(item_category__iexact='Jumper')
    #Country
    if 'Continent' in request.GET:
        countries = request.GET['Continent']
        if countries:
            queryset_list = queryset_list.filter(item_continent__iexact=countries)
    queryset_list = queryset_list.filter(item_gender__iexact='Female', item_category__iexact='Jumper')
    paginator = Paginator(queryset_list, 16, orphans=4)
    my_total_searched = queryset_list.count()
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)
    context = {
        'CATEGORY_CHOICES_FEMALE': CATEGORY_CHOICES_FEMALE,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
        'my_total_searched': my_total_searched,
        'my_total_men_count': my_total_men_count,
        'my_total_woman_count': my_total_woman_count,
        'my_total_kid_count': my_total_kid_count,
        'my_total_uni_count': my_total_uni_count,
    }
    return render(request, 'search-womens-tops.html', context)

def filter_womens_tops(request):

    context = {
        'CATEGORY_CHOICES_FEMALE': CATEGORY_CHOICES_FEMALE,
        'CONTINENT_CHOICES': CONTINENT_CHOICES,
    }

    return render(request, 'filter-womens-tops.html', context)
