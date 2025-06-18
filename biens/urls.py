from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_biens, name='liste_biens'),
]
