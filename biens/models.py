from django.db import models
from utilisateurs.models import Utilisateur

class TypeBien(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class BienImmobilier(models.Model):
    STATUTS = [
        ('disponible', 'Disponible'),
        ('loue', 'Loué'),
        ('vendu', 'Vendu'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    proprietaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='biens_possedes')
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    type_bien = models.ForeignKey(TypeBien, on_delete=models.SET_NULL, null=True)
    adresse = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUTS, default='disponible')
    image = models.ImageField(upload_to='images_biens/', blank=True, null=True)

    def __str__(self):
        return self.titre
