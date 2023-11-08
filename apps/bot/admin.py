from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.bot.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['user_id']
