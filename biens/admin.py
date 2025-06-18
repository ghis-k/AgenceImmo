from django.contrib import admin
from .models import BienImmobilier, TypeBien

@admin.register(BienImmobilier)
class BienImmobilierAdmin(admin.ModelAdmin):
    list_display = ('titre', 'type_bien', 'prix', 'statut', 'proprietaire')
    list_filter = ('statut', 'type_bien')
    search_fields = ('titre', 'adresse')

@admin.register(TypeBien)
class TypeBienAdmin(admin.ModelAdmin):
    list_display = ('nom',)
