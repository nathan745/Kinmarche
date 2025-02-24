from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    telephone = forms.CharField(max_length=15, required=False)
    adresse = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'telephone', 'adresse', 'password1', 'password2']

class ConnexionForm(AuthenticationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'password']
