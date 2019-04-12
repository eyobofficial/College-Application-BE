from django.db import models

from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
