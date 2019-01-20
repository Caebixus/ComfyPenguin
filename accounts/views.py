from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # Uživatel má informace a chce založit účet
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['usernameEmail'])
                return render(request, 'accounts/signup.html', {'error':'Uživatel s tímto emailem již existuje - '})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['usernameEmail'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('profile')
        else:
            return render(request, 'signup.html', {'error':'Hesla nesouhlasí'})
    else:
            # Uživatel má informace a chce založit účet
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['usernameEmail'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Zadané údaje nesedí s uloženými'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')

def profile(request):
    args = {'user':request.user}
    return render(request, 'profile.html', args)
