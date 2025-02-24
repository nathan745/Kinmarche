from django.urls import path
from . import views


urlpatterns = [
    path('List/',views.ProductsListView.as_view(), name = 'product.list'),
    path('detail/<int:pk>', views.ProductdetaiView.as_view(), name = 'product.detail'),
     path('recherche/', views.rechercher_produits, name='recherche_produits'),
]
