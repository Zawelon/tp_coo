#Creation de la View
from django.views.generic import DetailView
from django.http import JsonResponse
from .models import * #Importation de toutes les classe crees dans le fichier models.py
from django.shortcuts import render, get_object_or_404


class VilleJsonDetailView(DetailView):
    model = Ville

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class UsineJsonDetailView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class ProduitJsonDetailView(DetailView):
    model = Produit

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


def produire_produit(request, produit_id, quantite):
    usine = Usine.objects.first()  
    produit = get_object_or_404(Produit, id=produit_id)
    usine.approvisionnement_automatique(produit, quantite)

    return render(request, 'production.html', {
        'usine': usine,
        'produit': produit,
        'quantite': quantite
    })
