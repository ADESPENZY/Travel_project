from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(max_length=200)
    has_profile = models.BooleanField(default=False)
