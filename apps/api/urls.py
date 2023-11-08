from django.urls import path, include

from apps.api.views import DeliveredApi, VeterinarianApi
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register("delivered", DeliveredApi)
routers.register("veterinarian", VeterinarianApi)

urlpatterns = [
    path("api/", include(routers.urls)),
]
