from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    ROLES = [
        ('admin', 'Administrateur'),
        ('agent', 'Agent immobilier'),
        ('client', 'Client'),
        ('proprietaire', 'Propriétaire'),
    ]
    role = models.CharField(max_length=20, choices=ROLES)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
