from django.shortcuts import render


def liste_biens(request):
    type_id = request.GET.get('type')
    biens = BienImmobilier.objects.filter(statut='disponible')
    types = TypeBien.objects.all()

    if type_id:
        biens = biens.filter(type_bien_id=type_id)

    return render(request, 'biens/liste.html', {
        'biens': biens,
        'types': types
    })
