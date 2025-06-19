from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('bien', 'type_transaction', 'prix_final', 'client', 'agent', 'date', 'statut')
    list_filter = ('type_transaction', 'statut')
    search_fields = ('client__username', 'bien__titre')
