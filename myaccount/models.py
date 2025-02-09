from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = ' کاربر ها'