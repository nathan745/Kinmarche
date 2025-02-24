from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView
from .models import Produit
from django.db.models import Q


# Create your views here.

class ProductsListView(ListView):
    model = Produit
    context_object_name = 'produits'
    template_name = 'product/shop.html'




class ProductdetaiView(DetailView):
    model = Produit
    context_object_name = 'product'
    template_name = 'product/shop-detail.html'



def handler404(request, exception):

    return render(request, 'product/404.html')

def rechercher_produits(request):
    query = request.GET.get('q', '')  # Récupère la recherche de l'utilisateur
    produits = Produit.objects.all()

    if query:
        produits = produits.filter(
            Q(nom__icontains=query) | 
            Q(description__icontains=query)
        )  # Recherche par nom ou description (insensible à la casse)

    return render(request, 'product/recherche.html', {'produits': produits, 'query': query})