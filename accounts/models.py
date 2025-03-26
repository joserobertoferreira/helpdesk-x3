from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    customer = models.CharField(max_length=5, blank=True, null=True, verbose_name='Empresa')
