# vitrine/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bien, TypeBien
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from transactions.models import Transaction



def locations(request):
    type_list = TypeBien.objects.all()
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



@login_required(login_url='login')
def reserver_bien(request, id):
    bien = get_object_or_404(Bien, pk=id)

    if bien.statut == 'loue':
        messages.error(request, "Ce bien est déjà loué.")
        return redirect('locations')

    if request.method == 'POST':
        # Créer la transaction
        Transaction.objects.create(
            bien=bien,
            client=request.user,
            type_transaction='location',
            prix_final=bien.prix,
            statut='en attente'
        )
        bien.statut = 'loue'
        bien.save()
        messages.success(request, "Votre demande de location a été enregistrée.")
        return redirect('locations')

    return render(request, 'vitrine/reserver.html', {'bien': bien})



@login_required(login_url='/login/')
def acheter_bien(request, id):
    bien = get_object_or_404(Bien, id=id)

    if request.method == 'POST':
        if bien.statut != 'vendu':
            Transaction.objects.create(
                bien=bien,
                client=request.user,
                agent=None,
                type_transaction='achat',
                prix_final=bien.prix,
                statut='en attente'
            )
            bien.statut = 'vendu'
            bien.save()

            messages.success(request, "Achat enregistré avec succès.")
            return render(request, 'vitrine/merci.html', {'nom': request.user.username})

    return render(request, 'vitrine/acheter.html', {'bien': bien})



@login_required
def ajouter_bien(request):
    if not request.user.is_staff:
        messages.error(request, "Vous n'avez pas l'autorisation d'accéder à cette page.")
        return redirect('accueil')

    types = TypeBien.objects.all()

    if request.method == 'POST':
        titre = request.POST.get('titre')
        ville = request.POST.get('ville')
        surface = request.POST.get('surface')
        prix = request.POST.get('prix')
        image = request.FILES.get('image')
        type_id = request.POST.get('type')

        type_obj = TypeBien.objects.get(id=type_id)

        bien = Bien(
            titre=titre,
            ville=ville,
            surface=surface,
            prix=prix,
            image=image,
            type=type_obj,
            statut='disponible',  # mettre la valeur par défaut que tu veux
            proprietaire=request.user
        )
        bien.save()
        messages.success(request, "Bien ajouté avec succès !")
        return redirect('locations')

    return render(request, 'vitrine/ajouter_bien.html', {'types': types})




