from .models import Panier

def panier_context(request):
    if request.user.is_authenticated:
        panier = Panier.objects.filter(user=request.user).first()
        panier_count = sum(item.quantite for item in panier.items.all()) if panier else 0
    else:
        panier_count = 0  # Si l'utilisateur n'est pas connecté, le panier est vide

    return {"panier_count": panier_count}
