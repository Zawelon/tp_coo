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

# pour la partie ApiView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


# JSON Views (héritage de DetailView)
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


class LocalJsonDetailView(DetailView):
    model = Local

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class SiegeSocialJsonDetailView(DetailView):
    model = SiegeSocial

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class MachineJsonDetailView(DetailView):
    model = Machine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class ObjetJsonDetailView(DetailView):
    model = Objet

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class StockJsonDetailView(DetailView):
    model = Stock

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class RessourceJsonDetailView(DetailView):
    model = Ressource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class QuantiteRessourceJsonDetailView(DetailView):
    model = QuantiteRessource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


class EtapeJsonDetailView(DetailView):
    model = Etape

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json(), **response_kwargs)


# API Views (héritage de DRF)
class VilleApiView(APIView):
    def get(self, request, pk):
        ville = get_object_or_404(Ville, pk=pk)
        return Response(ville.json())


class UsineApiView(APIView):
    def get(self, request, pk):
        usine = get_object_or_404(Usine, pk=pk)
        return Response(usine.json())


class ProduitApiView(APIView):
    def get(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        return Response(produit.json())


class LocalApiView(APIView):
    def get(self, request, pk):
        local = get_object_or_404(Local, pk=pk)
        return Response(local.json())


class SiegeSocialApiView(APIView):
    def get(self, request, pk):
        siege_social = get_object_or_404(SiegeSocial, pk=pk)
        return Response(siege_social.json())


class MachineApiView(APIView):
    def get(self, request, pk):
        machine = get_object_or_404(Machine, pk=pk)
        return Response(machine.json())


class ObjetApiView(APIView):
    def get(self, request, pk):
        objet = get_object_or_404(Objet, pk=pk)
        return Response(objet.json())


class StockApiView(APIView):
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return Response(stock.json())


class RessourceApiView(APIView):
    def get(self, request, pk):
        ressource = get_object_or_404(Ressource, pk=pk)
        return Response(ressource.json())


class QuantiteRessourceApiView(APIView):
    def get(self, request, pk):
        quantite_ressource = get_object_or_404(QuantiteRessource, pk=pk)
        return Response(quantite_ressource.json())


class EtapeApiView(APIView):
    def get(self, request, pk):
        etape = get_object_or_404(Etape, pk=pk)
        return Response(etape.json())
