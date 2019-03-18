from django.shortcuts import render
from clothes.models import Product_Clothes
from comfy.choices import GENDER_CHOICES, CATEGORY_CHOICES
from comfy.views import search
from django.core.paginator import Paginator

# Create your views here.

def searchpage(request):
    listing = Product_Clothes.objects.all()[:8]
    my_total = Product_Clothes.objects.count()

# counting Mans clothes
    my_total_men = Product_Clothes.objects.filter(item_gender__iexact="Male")
    my_total_men_count = my_total_men.count()

# counting Mans clothes
    my_total_woman = Product_Clothes.objects.filter(item_gender__iexact="Female")
    my_total_woman_count = my_total_woman.count()

# counting Mans clothes
    my_total_kid = Product_Clothes.objects.filter(item_gender__iexact="Kids")
    my_total_kid_count = my_total_kid.count()

# counting Mans clothes
    my_total_uni = Product_Clothes.objects.filter(item_gender__iexact="Unisex")
    my_total_uni_count = my_total_uni.count()


    queryset_list = Product_Clothes.objects.order_by('?')

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

    #Gender
    if 'Gender' in request.GET:
        genders = request.GET['Gender']
        if genders:
            queryset_list = queryset_list.filter(item_gender__iexact=genders)

    #Type
    if 'Type' in request.GET:
        types = request.GET['Type']
        if types:
            queryset_list = queryset_list.filter(item_category__iexact=types)

    paginator = Paginator(queryset_list, 16, orphans=4)

    my_total_searched = queryset_list.count()

    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
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
    print(context)
    return render(request, 'search.html', context)

def filter(request):

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
    }

    return render(request, 'filter.html', context)
