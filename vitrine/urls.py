from django.urls import path
from . import views
from .views import ajouter_bien
urlpatterns = [
    path('', views.locations, name='locations'),  # Ceci est la vue de la page d'accueil
    path('louer/<int:id>/', views.reserver_bien, name='reserver_bien'),
    path('acheter/<int:id>/', views.acheter_bien, name='acheter_bien'),
    path('ajouter/', ajouter_bien, name='ajouter_bien'),
]