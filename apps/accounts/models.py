from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    ROLE = (
        (1, "Veterenar"),
        (2, "Yetkazib beruvchi")
    )

    role = models.IntegerField(choices=ROLE, null=True, blank=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User")
