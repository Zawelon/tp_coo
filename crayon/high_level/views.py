from .models import Ville, Usine, Machine
from django.views.generic import DetailView
from django.http import JsonResponse


class VilleJsonDetailView(DetailView):
    model = Ville

    def render_to_reponse(self):
        return JsonResponse(self.object.json())


class UsineJsonDetailView(DetailView):
    model = Usine

    def render_to_reponse(self):
        return JsonResponse(self.object.json())


class MachineJsonDetailView(DetailView):
    model = Machine

    def render_to_reponse(self):
        return JsonResponse(self.object.json())
