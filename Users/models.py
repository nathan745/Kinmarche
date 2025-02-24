
from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username
