from django.contrib import admin
from .models import Produit
from django.utils.html import format_html
from django.urls import reverse

class ProduitAdmin(admin.ModelAdmin):
    # Colonnes affichées dans l'admin
    list_display = ('nom', 'prix', 'stock', 'image', 'voir_sur_site')  
    search_fields = ('nom',)  # Barre de recherche par nom
    list_filter = ('prix',)  # Ajoute des filtres par prix

    # Fonction pour afficher un lien vers la page produit
    def voir_sur_site(self, obj):
        url = reverse('product.detail', args=[obj.pk])  # Assure-toi que 'product.detail' est bien le nom de ta vue
        return format_html('<a href="{}" target="_blank">Voir sur le site</a>', url)

    voir_sur_site.short_description = "Aperçu"  # Description du lien dans l'admin

# Enregistrement du modèle et de l'admin
admin.site.register(Produit, ProduitAdmin)