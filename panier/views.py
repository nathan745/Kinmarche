from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.urls import reverse_lazy
from .models import Panier, PanierItem
from Orders.models import Commande, CommandeProduit
from Products.models import Produit
from .forms import CommandeForm

@login_required(login_url=reverse_lazy("connexion"))
def afficher_panier(request):
    panier, _ = Panier.objects.get_or_create(user=request.user)
    items = panier.items.select_related("produit").all()
    total_panier = sum(item.produit.prix * item.quantite for item in items)
    items_count = sum(item.quantite for item in items)

    return render(request, "panier/cart.html", {
        "items": items,
        "total_panier": total_panier,
        "items_count": items_count
    })

@login_required(login_url=reverse_lazy("connexion"))
def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    panier, _ = Panier.objects.get_or_create(user=request.user)

    item, created = PanierItem.objects.get_or_create(panier=panier, produit=produit)
    if not created:
        item.quantite += 1
        item.save()
    
    return redirect("afficher_panier")

@login_required(login_url=reverse_lazy("connexion"))
def diminuer_quantite(request, produit_id):
    panier = Panier.objects.filter(user=request.user).first()
    if not panier:
        return redirect("afficher_panier")
    
    item = PanierItem.objects.filter(panier=panier, produit_id=produit_id).first()
    if item:
        if item.quantite > 1:
            item.quantite -= 1
            item.save()
        else:
            item.delete()
    
    return redirect("afficher_panier")

@login_required(login_url=reverse_lazy("connexion"))
def supprimer_du_panier(request, item_id):
    item = get_object_or_404(PanierItem, id=item_id)
    
    if item.panier.user != request.user:
        messages.error(request, "Action non autorisée.")
        return redirect("afficher_panier")

    item.delete()
    return redirect("afficher_panier")

@login_required(login_url=reverse_lazy("connexion"))
def checkout(request):
    panier = Panier.objects.filter(user=request.user).first()
    
    if not panier or not panier.items.exists():
        messages.warning(request, "Votre panier est vide.")
        return redirect("afficher_panier")

    total_panier = sum(item.produit.prix * item.quantite for item in panier.items.all())
    
    return render(request, "panier/checkout.html", {
        "total_panier": total_panier
    })
@login_required(login_url='connexion')
def passer_commande(request):
    panier = Panier.objects.filter(user=request.user).first()

    if not panier or not panier.items.exists():
        messages.error(request, "Votre panier est vide.")
        return redirect("afficher_panier")

    # Vérification du stock avant la commande
    for item in panier.items.all():
        if item.produit.stock < item.quantite:
            messages.error(request, f"Le produit {item.produit.nom} est en rupture de stock.")
            return redirect("afficher_panier")

    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            commande.client = request.user
            commande.save()

            for item in panier.items.all():
                CommandeProduit.objects.create(
                    commande=commande,
                    produit=item.produit,
                    quantite=item.quantite
                )

            # Vider le panier après la commande
            panier.items.all().delete()

            messages.success(request, "Votre commande a été passée avec succès !")
            return redirect('confirmation_commande', commande_id=commande.id)
    else:
        form = CommandeForm()

    return render(request, 'panier/passer_commande.html', {'form': form})

@login_required(login_url=reverse_lazy("connexion"))
def confirmation_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    
    if commande.client != request.user:
        messages.error(request, "Vous n'avez pas accès à cette commande.")
        return redirect("afficher_panier")

    total_commande = sum(item.produit.prix * item.quantite for item in commande.commandeproduit_set.all())
    
    return render(request, "panier/C.html", {
        "commande": commande,
        "total_commande": total_commande
    })
