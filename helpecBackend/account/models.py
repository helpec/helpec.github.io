from django.contrib.auth.models import AbstractUser
from django.db import models

class HP_User(AbstractUser):
    phone = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email