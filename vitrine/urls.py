from django.urls import path
from . import views

urlpatterns = [
    path('', views.locations, name='locations'),  # Ceci est la vue de la page d'accueil
    path('louer/<int:id>/', views.reserver_bien, name='reserver_bien'),
    path('acheter/<int:id>/', views.acheter_bien, name='acheter_bien'),
]