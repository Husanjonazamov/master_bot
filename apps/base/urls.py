from django.urls import path

from apps.base.views import switch_lang

urlpatterns = [
    path("setlang/", switch_lang, name="set_language"),
]
