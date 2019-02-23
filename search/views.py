from django.shortcuts import render
from clothes.models import Product_Clothes
from comfy.choices import GENDER_CHOICES, CATEGORY_CHOICES
from comfy.views import search
from django.core.paginator import Paginator

# Create your views here.

def searchpage(request):
    listing = Product_Clothes.objects.all()[:8]
    my_total = Product_Clothes.objects.count()
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

    paginator = Paginator(queryset_list, 4, orphans=4)

    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'listing': queryset_list,
        'my_total': my_total,
        'values': request.GET,
        'paginationing': paginationing,
    }
    return render(request, 'search.html', context)

def filter(request):

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
    }

    return render(request, 'filter.html', context)
