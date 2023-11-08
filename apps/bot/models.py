from django.db import models

from apps.accounts.models import User as DUser


# Create your models here.
class User(models.Model):
    user_id = models.BigIntegerField()
    token = models.CharField(max_length=255, null=True, blank=True)
    is_login = models.BooleanField(default=False)
    profile = models.ForeignKey(DUser, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = "Bot Foydalanuvchilari"
        verbose_name_plural = "Bot Foydalanuvchilari"
