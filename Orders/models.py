from django.db import models
from Products.models import Produit
from django.conf import settings

class Commande(models.Model):
    STATUT_CHOICES = [
        ('en attente', 'En attente de paiement'),
        ('confirmée', 'Confirmée'),
        ('préparée', 'Préparée'),
        ('en livraison', 'En livraison'),
        ('livrée', 'Livrée'),
        ('annulée', 'Annulée'),
    ]

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through="CommandeProduit")
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en attente')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    livreur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="livraisons")

    def __str__(self):
        return f"Commande {self.id} - {self.client.username} - {self.get_statut_display()}"

    def calculer_total(self):
        total = sum(item.produit.prix * item.quantite for item in self.commandeproduit_set.all())
        self.total = total
        self.save()

class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} (Commande {self.commande.id})"
