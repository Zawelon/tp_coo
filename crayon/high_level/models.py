# election/models.py
from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    prix_par_m2 = models.IntegerField()

    def __str__(self):
        return self.nom
