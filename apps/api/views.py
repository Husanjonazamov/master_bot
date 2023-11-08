from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet

from apps.api.models import Delivered, Veterinarian
from apps.api.serializers import DeliveredSerializer, VeterinarianSerializer


class DeliveredApi(ModelViewSet):
    serializer_class = DeliveredSerializer
    queryset = Delivered.objects.all()


class VeterinarianApi(ModelViewSet):
    serializer_class = VeterinarianSerializer
    queryset = Veterinarian.objects.all()