from django.urls import path
from .views import afficher_panier, ajouter_au_panier, diminuer_quantite, supprimer_du_panier, checkout,passer_commande, confirmation_commande

urlpatterns = [
    path('passer_commande/', passer_commande, name="passer_commande"),
    path('panier/', afficher_panier, name='afficher_panier'),
    path('ajouter_au_panier/<int:produit_id>/', ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/diminuer-quantite/<int:produit_id>/', diminuer_quantite, name='diminuer_quantite'),
    path('panier/supprimer/<int:item_id>/', supprimer_du_panier, name='supprimer_du_panier'),
    path('checkout/', checkout, name='checkout'),
    path('confirmation_commande/<int:commande_id>/', confirmation_commande, name='confirmation_commande'),
]
