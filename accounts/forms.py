from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
        'username',
        )
