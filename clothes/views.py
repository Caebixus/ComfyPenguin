from django.shortcuts import render

# Create your views here.

def clothespage(request):
    return render(request, 'Create-clothes.html')
