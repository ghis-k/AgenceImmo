# vitrine/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bien, Type
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def locations(request):
    type_list = Type.objects.all()
    biens = Bien.objects.all()

    if request.GET.get("type"):
        biens = biens.filter(type_id=request.GET["type"])
    if request.GET.get("ville"):
        biens = biens.filter(ville__icontains=request.GET["ville"])
    if request.GET.get("loyer_max"):
        biens = biens.filter(prix__lte=request.GET["loyer_max"])
    if request.GET.get("surface_min"):
        biens = biens.filter(surface__gte=request.GET["surface_min"])

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "biens": biens,
        "type_list": type_list,
        "form": form
    }
    return render(request, "vitrine/locations.html", context)

def reserver_bien(request, id):
    bien = get_object_or_404(Bien, id=id)
    
    if request.method == 'POST':
        # Ici tu traites le formulaire de location (à créer)
        # Exemple simple :
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Tu peux ici enregistrer la demande en base de données ou envoyer un mail

        return render(request, 'vitrine/merci.html', {'nom': nom})

    return render(request, 'vitrine/reserver.html', {'bien': bien})



def acheter_bien(request, id):
    bien = get_object_or_404(Bien, id=id)

    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Ici tu peux ajouter un traitement (ex: enregistrer commande, envoyer mail...)

        # Exemple: marquer le bien comme vendu (optionnel)
        bien.vendu = True
        bien.save()

        return render(request, 'vitrine/merci.html', {'nom': nom, 'bien': bien})

    return render(request, 'vitrine/acheter.html', {'bien': bien})


@login_required
def ajouter_bien(request):
    if not request.user.is_staff:
        messages.error(request, "Vous n'avez pas l'autorisation d'accéder à cette page.")
        return redirect('accueil')

    types = Type.objects.all()

    if request.method == 'POST':
        titre = request.POST.get('titre')
        ville = request.POST.get('ville')
        surface = request.POST.get('surface')
        prix = request.POST.get('prix')
        image = request.FILES.get('image')
        type_id = request.POST.get('type')

        type_obj = Type.objects.get(id=type_id)

        bien = Bien(
            titre=titre,
            ville=ville,
            surface=surface,
            prix=prix,
            image=image,
            type=type_obj,
            vendu=False,
        )
        bien.save()
        messages.success(request, "Bien ajouté avec succès !")
        return redirect('locations')

    return render(request, 'vitrine/ajouter_bien.html', {'types': types})


