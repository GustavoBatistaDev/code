from django import forms
from django.contrib.auth import forms as auth_forms

from .models import User


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ('email',)


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'email')
