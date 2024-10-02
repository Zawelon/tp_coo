from .models import Ville
from django.views.generic import DetailView
from django.http import JsonResponse


class VilleJsonDetailView(DetailView):
    model = Ville

    def render_to_reponse(self):
        return JsonResponse(self.object.json())
