from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer
from apps.api.models import Delivered, Location, Veterinarian


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "lat",
            "lon"
        ]


class DeliveredSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Delivered
        fields = [
            "user",
            "first_name",
            "phone",
            "location",
            "product_count",
            "addition",
        ]

    def create(self, validated_data):
        location = Location.objects.create(lat=validated_data.get("location").get("lat"),
                                           lon=validated_data.get("location").get("lon"))
        validated_data['location'] = location
        res = Delivered.objects.create(**validated_data)
        return res


class VeterinarianSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Veterinarian
        fields = [
            "user",
            "user_id",
            "first_name",
            "location",
            "moisture",
            "temperature",
            "day",
            "conclusion",
            "addition",
        ]

    def create(self, validated_data):
        location = Location.objects.create(lat=validated_data.get("location").get("lat"),
                                           lon=validated_data.get("location").get("lon"))
        validated_data['location'] = location

        user = get_object_or_404(User, id=validated_data.pop("user_id"))
        validated_data["user"] = user

        res = Veterinarian.objects.create(**validated_data)
        return res
