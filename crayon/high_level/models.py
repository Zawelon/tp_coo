# election/models.py
from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix_par_m2 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville,
        on_delete=models.CASCADE,
    )
    surface = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom


# 总部模型 (SiègeSocial)
class SiegeSocial(Local):
    pass


# 机器模型 (Machine)
class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    n_serie = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


# 资源模型 (Class Objet)
class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom


# 工厂模型 (Usine)
class Usine(models.Model):
    machines = models.ManyToManyField(Machine)

    def __str__(self):
        return self.nom


# 资源模型 (Ressource)
class Ressource(Objet):
    pass


# 资源数量模型 (QuantiteRessource)
class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantite} de {self.ressource.nom}"


# 步骤模型 (Etape)
class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_ressource = models.ForeignKey(QuantiteRessource, on_delete=models.CASCADE)
    duree = models.IntegerField()  # 单位：分钟
    etape_suivante = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="precedente",
    )

    def __str__(self):
        return self.nom


# 产品模型 (Produit)
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


# 库存模型 (Stock)
class Stock(models.Model):
    objet = models.ForeignKey(Objet, on_delete=models.CASCADE)
    nombre = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.objet.nom}"
