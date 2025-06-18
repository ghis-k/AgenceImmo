# vitrine/models.py
from django.db import models

class Type(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Bien(models.Model):
    titre = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    surface = models.IntegerField()
    prix = models.IntegerField()
    image = models.ImageField(upload_to='biens/')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    vendu = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom}"
