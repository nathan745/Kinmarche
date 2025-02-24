from django import forms
from Orders.models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client', 'statut']

    adresse_livraison = forms.CharField(max_length=255, required=True)
    date_livraison = forms.DateTimeField(required=True)

    def save(self, commit=True):
        # Créer la commande avec les produits dans le panier
        commande = super().save(commit=False)
        if commit:
            commande.save()
        return commande
