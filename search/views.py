from django.shortcuts import render

# Create your views here.

def searchpage(request):
    return render(request, 'search.html')
