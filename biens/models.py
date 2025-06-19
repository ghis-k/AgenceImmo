#from django.db import models
#from utilisateurs.models import Utilisateur

#class TypeBien(models.Model):
 #   nom = models.CharField(max_length=100)

  #  def __str__(self):
   #     return self.nom

#class Bien(models.Model):
 #   STATUTS = [
  #      ('disponible', 'Disponible'),
   #     ('loue', 'Loué'),
    #    ('vendu', 'Vendu'),
    #]

    
    #titre = models.CharField(max_length=200)
    #ville = models.CharField(max_length=100)
    #surface = models.PositiveIntegerField()
    #prix = models.DecimalField(max_digits=12, decimal_places=2)
    #image = models.ImageField(upload_to='images/')
    #type = models.ForeignKey(TypeBien, on_delete=models.CASCADE)
    #statut = models.CharField(max_length=10, choices=STATUTS, default='disponible')  # Nouveau champ
    #description = models.TextField()
    #proprietaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='biens_possedes')
    #prix = models.DecimalField(max_digits=12, decimal_places=2)
    #adresse = models.TextField()


    #def __str__(self):
     #   return self.titre
