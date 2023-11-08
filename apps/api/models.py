from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from import_export.admin import ExportMixin

from apps.accounts.models import User

class Registration(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()

    class Meta:
        verbose_name = _("Registration")
        verbose_name_plural = _("Registration")

    def __str__(self):
        return self.name



class Location(models.Model):
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.lat, self.lon)

class Placing(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150)
    phone = models.IntegerField()
    day = models.DateField()
    product_count = models.IntegerField()
    location = models.OneToOneField(Location, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Placing")
        verbose_name_plural = _("Placing")


    def __str__(self) -> str:
        return self.name


class Delivered(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField()
    location = models.OneToOneField(Location, on_delete=models.DO_NOTHING)
    product_count = models.IntegerField(null=True, blank=True)
    image = models.ImageField()
    addition = models.FileField(blank=True, null=True, upload_to="additions/")
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Delivered")
        verbose_name_plural = _("Delivered")


class Veterinarian(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone = models.IntegerField()
    first_name = models.CharField(max_length=255)
    location = models.OneToOneField(Location, on_delete=models.DO_NOTHING)
    moisture = models.IntegerField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)   
    diagnosis = models.TextField(null=True, blank=True)
    addition = models.FileField(blank=True, null=True, upload_to="additions/")
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Veterinarians")
        verbose_name_plural = _("Veterinarians")
