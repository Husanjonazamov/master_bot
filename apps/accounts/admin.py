from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User
from .forms import CustomUserCreationForm
from django import forms


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Qo\'shimcha', {'fields': ('role',)}),
    )


admin.site.register(User, CustomUserAdmin)
