from django.contrib import admin
from .models import Produit

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'image')  # Colonnes affichées dans l'admin
    search_fields = ('nom',)  # Barre de recherche par nom
    list_filter = ('prix',)  # Ajoute des filtres par prix

admin.site.register(Produit, ProduitAdmin)

