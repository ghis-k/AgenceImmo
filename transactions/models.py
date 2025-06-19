from django.db import models
from vitrine.models import Bien
from utilisateurs.models import Utilisateur


class Transaction(models.Model):
    TYPES = [
        ('location', 'Location'),
        ('achat', 'Achat'),
    ]

    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='transactions_client')
    agent = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_agent')
    date = models.DateTimeField(auto_now_add=True)
    type_transaction = models.CharField(max_length=10, choices=TYPES)
    prix_final = models.DecimalField(max_digits=12, decimal_places=2)
    statut = models.CharField(max_length=50, default='en attente')

    def __str__(self):
        return f"{self.bien} - {self.type_transaction}"
