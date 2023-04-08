from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.db import models

#
# class CustomUserManager(BaseUserManager):

class CustomUser(AbstractUser):
    # username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
