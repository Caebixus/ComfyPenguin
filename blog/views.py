from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'interesting-facts.html',)

def clanek1(request):
    return render(request, 'clanek1.html',)
