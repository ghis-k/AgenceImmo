# vitrine/forms.py
from django import forms
from .models import MessageContact
from .models import Bien  # importe ton modèle Bien depuis le fichier models.py local

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'message']


class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ['titre', 'ville', 'surface', 'prix', 'image', 'type','vendu']
