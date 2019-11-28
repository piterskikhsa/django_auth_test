from django.db import models
from django.contrib.auth.models import AbstractUser
from simpleapp.managers import SimpleUserManager


class SimpleUser(AbstractUser):
    username = models.CharField('username', max_length=100)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = SimpleUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name
