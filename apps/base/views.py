from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import activate
from rest_framework.views import APIView

from apps.accounts.models import User
from apps.api.models import Delivered, Veterinarian


def switch_lang(request):
    lang = request.POST.get("language")
    if lang in [lang[0] for lang in settings.LANGUAGES]:
        request.session[settings.LANGUAGE_SESSION_KEY] = lang
        activate(lang)
    return redirect(request.META.get('HTTP_REFERER', '/'))
