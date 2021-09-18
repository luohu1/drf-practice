from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    nickname = models.CharField(max_length=64, null=False, verbose_name=_('nickname'))
    first_name = None
    last_name = None

    class Meta:
        ordering = ['-pk']

    def __str__(self) -> str:
        return self.username
