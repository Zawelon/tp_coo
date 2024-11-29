from django.db import models
from datetime import timedelta


######################CLASS Ville################
class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix_par_m2 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

    def json_extended(self):
        return {
            "nom": self.nom,
            "code_postal": self.code_postal,
            "prix_par_m2": str(self.prix_par_m2),
        }


######################CLASS Local################
class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville,
        on_delete=models.CASCADE,
    )
    surface = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "ville": self.ville.json_extended(),
            "surface": str(self.surface),
        }

    """
    class Meta:
        abstract = True #Pour definir une class abstraite
    """


######################CLASS SiegeSocial################
class SiegeSocial(Local):
    pass


######################CLASS Machine################
class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    n_serie = models.CharField(max_length=100)

    def costs(self):
        return self.prix

    def __str__(self):
        return self.nom

    def json_extended(self):
        return {
            "nom": self.nom,
            "prix": str(self.prix),
            "nunero de serie": self.n_serie,
        }


######################CLASS Usine################
class Usine(Local):
    machines = models.ManyToManyField(Machine)

    def __str__(self):
        return self.nom

    # Calcul du cout d'une Usine
    def costs(self):
        area_cost = 0
        machines_cost = 0
        stock_cost = 0

        # Calcul du cout de la surface
        area_cost = self.surface * self.ville.prix_par_m2

        # Calcul du cout des machines
        for machine in self.machines.all():
            machines_cost += machine.costs()

        # Calcul du cout du stock
        for stock in self.stock_set.all():
            stock_cost += stock.costs()

        # Retourne la somme totale des couts
        return area_cost + machines_cost + stock_cost

    def json_extended(self):
        return {
            "nom": self.nom,
            "surface": str(self.surface),
            "ville": self.ville.json_extended(),
            "machines": [machine.json_extended() for machine in self.machines.all()],
            "stock": [stock.json_extended() for stock in self.stock_set.all()],
        }

    # Facultatif
    def approvisionnement_automatique(self, produit, quantite):
        etape = produit.premiere_etape
        while etape:
            ressource = etape.my_quantite_ressource.ressource
            quantite_needed = etape.my_quantite_ressource.quantite * quantite

            # Calcul de la quantite en stock avec une boucle explicite
            quantite_in_stock = 0
            for stock in self.stock_set.filter(objet=ressource):
                quantite_in_stock += stock.nombre

            # Si la quantite en stock est insuffisante, acheter la ressource manquante
            if quantite_in_stock < quantite_needed:
                self.acheter_ressource(ressource, quantite_needed - quantite_in_stock)

            # Passer a l'etape suivante
            etape = etape.etape_suivante

    # Facultatif
    # Mise a jour du stock
    def acheter_ressource(self, ressource, quantite):
        stock, created = self.stock_set.get_or_create(
            objet=ressource, defaults={"nombre": 0}
        )
        stock.nombre += quantite
        stock.save()  # savegarde de modif de stock


######################CLASS OBJET################
class Objet(models.Model):
    nom = models.CharField(
        max_length=100, unique=True
    )  # Assurer des noms uniques pour les objets
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nom

    def json(self):
        return {"nom": self.nom, "prix": str(self.prix)}  # GG


######################CLASS Ressource################
class Ressource(Objet):
    pass


######################CLASS QuantiteRessource##########
class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)

    def costs(self):
        return self.quantite * self.ressource.prix

    def __str__(self):
        return f"{self.quantite} de {self.ressource.nom}"

    def json_extended(self):
        return {
            "ressource": self.ressource.json(),
            "quantite": self.quantite,
        }


######################CLASS Etape################
class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    my_quantite_ressource = models.ForeignKey(
        QuantiteRessource, on_delete=models.CASCADE
    )
    duree = models.DurationField(default=timedelta())  # Valeur par défaut = 0 seconde
    etape_suivante = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="precedente",
    )

    def __str__(self):
        return self.nom

    def json_extended(self):
        return {
            "nom": self.nom,
            "machine": self.machine.json_extended(),
            "my_quantite_ressource": self.my_quantite_ressource.json_extended(),
            "duree": self.duree,
            "etape_suivante": self.etape_suivante.nom if self.etape_suivante else None,
        }


######################CLASS Produit################
class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    def json_extended(self):
        return {"nom": self.nom, "premiere_etape": self.premiere_etape.nom}


######################CLASS Stock################
class Stock(models.Model):
    objet = models.ForeignKey(Objet, on_delete=models.CASCADE)
    nombre = models.IntegerField(default=0)
    usine = models.ForeignKey(
        Usine, on_delete=models.CASCADE
    )  # Un stock est dans une Usine

    def costs(self):
        return self.objet.prix * self.nombre

    def json_extended(self):
        return {"objet": self.objet.nom, "nombre": self.nombre}
