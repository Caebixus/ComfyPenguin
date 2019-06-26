from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm
from django.contrib import auth
from comfy.choices import GENDER_CHOICES, CATEGORY_CHOICES, CONTINENT_CHOICES, CATEGORY_CHOICES_MALE, CATEGORY_CHOICES_FEMALE, CONTINENT_CHOICES_US, CATEGORY_CHOICES_COUNTRY
from django.contrib.auth.decorators import login_required
from .models import MyClothes
from django.utils import timezone

def signup(request):
    if request.method == 'POST':
        # Uživatel má informace a chce založit účet
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['usernameEmail'])
                return render(request, 'accounts/signup.html', {'error':'User already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['usernameEmail'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('profile')
        else:
            return render(request, 'signup.html', {'error':'Passwords does not match'})
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
            return render(request, 'login.html', {'error': 'The entered data does not match the saved data'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')

@login_required
def profile(request):
    products = MyClothes.objects.filter(item_user_id=request.user)
    my_total = MyClothes.objects.filter(item_user_id=request.user).count()
    queryset_list = MyClothes.objects.order_by('?')
    context = {
        'products': products,
        'my_total': my_total,
        'queryset_list': queryset_list,
    }
    return render(request, 'profile.html', context)

@login_required
def Create_comfy_clothes(request):
    if request.method == 'POST':
        if request.POST['item_title'] and request.POST['item_width'] and request.POST['item_length'] and request.POST['item_type'] and request.POST['item_gender']:
            myclothes = MyClothes()
            myclothes.item_title = request.POST['item_title']
            myclothes.item_width = request.POST['item_width']
            myclothes.item_length = request.POST['item_length']
            myclothes.item_category = request.POST['item_type']
            myclothes.item_gender = request.POST['item_gender']
            if request.POST['item_country']:
                myclothes.item_country = request.POST['item_country']
            else:
                pass
            if 'image_main' in request.FILES:
                myclothes.image_main = request.FILES['image_main']
            else:
                image_main = False
            myclothes.upload_date = timezone.datetime.now()
            myclothes.item_user = request.user
            myclothes.save()
            context = {
                'CATEGORY_CHOICES': CATEGORY_CHOICES,
                'GENDER_CHOICES': GENDER_CHOICES,
                'CATEGORY_CHOICES_COUNTRY': CATEGORY_CHOICES_COUNTRY,
                }
            return redirect('profile')
        else:
            error = "Required fields are: Title, Width, Length, Type, Gender"
            context = {
                'CATEGORY_CHOICES': CATEGORY_CHOICES,
                'GENDER_CHOICES': GENDER_CHOICES,
                'CATEGORY_CHOICES_COUNTRY': CATEGORY_CHOICES_COUNTRY,
                'error': error,
                }
            return render(request, 'Create-comfy-clothes.html', context)
    else:
        context = {
            'CATEGORY_CHOICES': CATEGORY_CHOICES,
            'GENDER_CHOICES': GENDER_CHOICES,
            'CATEGORY_CHOICES_COUNTRY': CATEGORY_CHOICES_COUNTRY,
            }
        return render(request, 'Create-comfy-clothes.html', context)

    context = {
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CATEGORY_CHOICES_COUNTRY': CATEGORY_CHOICES_COUNTRY,
        }
    return render(request, 'Create-comfy-clothes.html', context)

@login_required
def My_comfy_clothes(request, myclothes_id):
    product = get_object_or_404(MyClothes, pk=myclothes_id)

    context = {
        'product': product,
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'CATEGORY_CHOICES_COUNTRY': CATEGORY_CHOICES_COUNTRY,
    }

    return render(request, 'My-comfy-clothes.html', context)

@login_required
def Delete_comfy_clothes(request, myclothes_id):
    deleteObj = get_object_or_404(MyClothes, pk=myclothes_id)
    deleteObj.delete()
    context = {
        'deleteObj': deleteObj,
    }
    return render(request, 'Delete-comfy-clothes.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'Edit-profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'Change-password.html', args)
