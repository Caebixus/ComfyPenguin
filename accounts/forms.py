from django import forms
from .models import MyClothes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class EditProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    class Meta:
        model = User
        fields = (
        'username',
        )


class PostForm(forms.ModelForm):

    item_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    item_width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'in inches'}))
    item_length = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'in inches'}))
    image_main = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = MyClothes
        fields = [
        'item_title',
        'item_gender',
        'item_category',
        'item_width',
        'item_length',
        'image_main',
        ]
