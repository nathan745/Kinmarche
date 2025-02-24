from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import InscriptionForm, ConnexionForm
from .models import Utilisateur

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)  # Connexion automatique après inscription
            messages.success(request, "Inscription réussie !")
            return redirect('Home.index')  # Rediriger vers la page d'accueil ou autre page
    else:
        form = InscriptionForm()
    return render(request, 'user/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            utilisateur = authenticate(request, username=username, password=password)
            if utilisateur is not None:
                login(request, utilisateur)
                messages.success(request, "Connexion réussie !")
                return redirect('Home.index')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = ConnexionForm()
    return render(request, 'user/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    messages.success(request, "Déconnexion réussie !")
    return redirect('Home.index')
