from django.db import models

# Create your models here.

from django.db import models
from Products.models import Produit
from Users.models import Utilisateur

class Panier(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, blank=True)  # Ajoute ce champ
    session_id = models.CharField(max_length=255)  # Lié à la session utilisateur
    date_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Panier de {self.user if self.user else 'Session ' + self.session_id}"

class PanierItem(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, related_name="items")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"
