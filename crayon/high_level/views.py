# Creation de la View
# pour la partie DetailView
from django.views.generic import DetailView
from django.http import JsonResponse
from .models import (
    Ville,
    Usine,
    Produit,
    Local,
    SiegeSocial,
    Machine,
    Objet,
    Stock,
    Etape,
    QuantiteRessource,
    Ressource,
)  # Importation de toutes les classe crees dans le fichier models.py

"""
# pour la partie ApiView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
"""


# JSON Views (héritage de DetailView)
class VilleJsonDetailView(DetailView):
    model = Ville

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class UsineJsonDetailView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class ProduitJsonDetailView(DetailView):
    model = Produit

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class LocalJsonDetailView(DetailView):
    model = Local

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class SiegeSocialJsonDetailView(DetailView):
    model = SiegeSocial

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class MachineJsonDetailView(DetailView):
    model = Machine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class ObjetJsonDetailView(DetailView):
    model = Objet

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class StockJsonDetailView(DetailView):
    model = Stock

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class RessourceJsonDetailView(DetailView):
    model = Ressource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class QuantiteRessourceJsonDetailView(DetailView):
    model = QuantiteRessource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class EtapeJsonDetailView(DetailView):
    model = Etape

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())
