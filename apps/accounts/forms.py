from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['role', "first_name", "last_name"]
