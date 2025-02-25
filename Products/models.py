from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='', blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom 