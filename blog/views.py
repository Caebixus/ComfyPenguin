from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'interesting-facts.html',)

def clanek1(request):
    return render(request, 'clanek1.html',)

def clanek2(request):
    return render(request, 'clanek2.html',)

def clanek3(request):
    return render(request, 'clanek3.html',)

def clanek4(request):
    return render(request, 'clanek4.html',)

def clanek5(request):
    return render(request, 'clanek5.html',)
