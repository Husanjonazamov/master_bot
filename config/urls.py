from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.base.urls")),
    path("", include("apps.api.urls")),
    path("accounts/", include("djoser.urls")),
    path("accounts/", include('djoser.urls.authtoken')),

    re_path(r"media/(.*)", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"static/(.*)", serve, {"document_root": settings.STATIC_ROOT}),
]
