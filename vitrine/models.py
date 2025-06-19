from django.db import models
from utilisateurs.models import Utilisateur

STATUTS = [
    ('disponible', 'Disponible'),
    ('loue', 'Loué'),
    ('vendu', 'Vendu'),
]

class TypeBien(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Bien(models.Model):
    titre = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    surface = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    type = models.ForeignKey(TypeBien, on_delete=models.CASCADE)
    statut = models.CharField(max_length=10, choices=STATUTS, default='disponible')  # <-- ici STATUTS est défini avant
    description = models.TextField()
    proprietaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='biens_possedes')
    adresse = models.TextField()

    def __str__(self):
        return self.titre

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom}"
