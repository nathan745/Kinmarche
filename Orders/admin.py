from django.contrib import admin
from django.utils.html import format_html
from .models import Commande, CommandeProduit

class CommandeProduitInline(admin.TabularInline):
    """Permet d'afficher les produits associés à une commande dans l'admin."""
    model = CommandeProduit
    extra = 1
    readonly_fields = ('produit', 'quantite', 'prix_total')  # Rend ces champs non modifiables

    def prix_total(self, obj):
        return f"{obj.produit.prix * obj.quantite} $"
    prix_total.short_description = "Prix total"

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_commande', 'statut', 'total_affiche', 'livreur')
    list_filter = ('statut', 'date_commande', 'livreur')
    search_fields = ('client__username', 'id', 'livreur__username')
    ordering = ('-date_commande',)
    inlines = [CommandeProduitInline]
    list_editable = ('statut', 'livreur')
    readonly_fields = ('total_affiche',)  # Champ en lecture seule pour afficher le total

    def total_affiche(self, obj):
        return format_html(f"<b>{obj.total} $</b>")  # Format HTML pour mettre en gras
    total_affiche.short_description = "Total"

    actions = ["marquer_livree", "annuler_commande"]

    def marquer_livree(self, request, queryset):
        queryset.update(statut="Livrée")
        self.message_user(request, "Les commandes sélectionnées ont été marquées comme livrées.")
    marquer_livree.short_description = "Marquer comme livrée"

    def annuler_commande(self, request, queryset):
        queryset.update(statut="Annulée")
        self.message_user(request, "Les commandes sélectionnées ont été annulées.")
    annuler_commande.short_description = "Annuler la commande"

@admin.register(CommandeProduit)
class CommandeProduitAdmin(admin.ModelAdmin):
    list_display = ('commande', 'produit', 'quantite', 'prix_total')
    list_filter = ('commande', 'produit')
    search_fields = ('commande__id', 'produit__nom')

    def prix_total(self, obj):
        return f"{obj.produit.prix * obj.quantite} $"
    prix_total.short_description = "Prix total"
