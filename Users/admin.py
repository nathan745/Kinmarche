from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

class CustomUserAdmin(UserAdmin):
    model = Utilisateur
    list_display = ('username', 'email', 'adresse', 'telephone', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')  # Ajout des filtres utiles
    search_fields = ('username', 'email', 'telephone')  # Recherche sur plusieurs champs
    ordering = ('-date_joined',)  # Classement par date d'inscription (du plus récent au plus ancien)

    # Définition des champs à afficher et organiser dans l'admin
    fieldsets = (
        ("Informations de connexion", {'fields': ('username', 'email', 'password')}),
        ("Informations personnelles", {'fields': ('adresse', 'telephone')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Dates", {'fields': ('last_login', 'date_joined')}),
    )

    # Champs affichés lors de la création d'un nouvel utilisateur
    add_fieldsets = (
        ("Création d'utilisateur", {
            'classes': ('wide',),
            'fields': ('username', 'email', 'adresse', 'telephone', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    readonly_fields = ('date_joined', 'last_login')  # Empêcher la modification de ces champs

    actions = ["activer_utilisateurs", "desactiver_utilisateurs"]  # Ajout d'actions personnalisées

    def activer_utilisateurs(self, request, queryset):
        """Active les comptes sélectionnés."""
        queryset.update(is_active=True)
        self.message_user(request, "Les utilisateurs sélectionnés ont été activés.")
    activer_utilisateurs.short_description = "Activer les utilisateurs sélectionnés"

    def desactiver_utilisateurs(self, request, queryset):
        """Désactive les comptes sélectionnés."""
        queryset.update(is_active=False)
        self.message_user(request, "Les utilisateurs sélectionnés ont été désactivés.")
    desactiver_utilisateurs.short_description = "Désactiver les utilisateurs sélectionnés"

admin.site.register(Utilisateur, CustomUserAdmin)



admin.site.site_header = "Gestion du Supermarché"
admin.site.site_title = "Admin Supermarché"
admin.site.index_title = "Bienvenue sur le tableau de bord"
