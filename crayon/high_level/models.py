from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix_par_m2 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom
    
    def json(self):
        return {
            "nom": self.nom,
            "code_postal": self.code_postal,
            "prix_par_m2": str(self.prix_par_m2)
        }


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville,
        on_delete=models.CASCADE,
    )
    surface = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nom
     
    def json(self):
        return {
            "nom": self.nom,
            "ville": self.ville.nom,
            "surface": str(self.surface)
        }


class SiegeSocial(Local):
    pass


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    n_serie = models.CharField(max_length=100)

    def costs(self):
        return self.prix
    
    def __str__(self):
        return self.nom
    
    def json(self):
        return {
            "nom": self.nom,
            "prix": str(self.prix),
            "n_serie": self.n_serie
        }


class Usine(Local):
    machines = models.ManyToManyField(Machine)

    def costs(self):
        area_cost = self.surface * self.ville.prix_par_m2
        machines_cost = sum(machine.costs() for machine in self.machines.all())
        stock_cost = sum(stock.costs() for stock in self.stock_set.all())
        return area_cost + machines_cost + stock_cost

    def approvisionnement_automatique(self, produit, quantite):
        etape = produit.premiere_etape
        while etape:
            ressource = etape.quantite_ressource.ressource
            quantite_needed = etape.quantite_ressource.quantite * quantite
            quantite_in_stock = sum(stock.nombre for stock in self.stock_set.filter(objet=ressource))
            if quantite_in_stock < quantite_needed:
                self.acheter_ressource(ressource, quantite_needed - quantite_in_stock)
            etape = etape.etape_suivante

    def acheter_ressource(self, ressource, quantite):
        stock, created = self.stock_set.get_or_create(objet=ressource, defaults={'nombre': 0})
        stock.nombre += quantite
        stock.save()

    def json(self):
        return {
            "nom": self.nom,
            "surface": str(self.surface),
            "ville": self.ville.nom,
            "machines": [machine.nom for machine in self.machines.all()],
            "stock": [stock.json() for stock in self.stock_set.all()]
        }

    def __str__(self):
        return self.nom


class Objet(models.Model):
    nom = models.CharField(max_length=100, unique=True)  # Ensure unique names for objects
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def json(self):
        return {
            "nom": self.nom,
            "prix": str(self.prix)
        }
    
    def __str__(self):
        return self.nom


class Ressource(Objet):
    pass


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)

    def costs(self):
        return self.quantite * self.ressource.prix

    def __str__(self):
        return f"{self.quantite} de {self.ressource.nom}"


class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_ressource = models.ForeignKey(QuantiteRessource, on_delete=models.CASCADE)
    duree = models.IntegerField()
    etape_suivante = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="precedente",
    )

    def json(self):
        return {
            "nom": self.nom,
            "machine": self.machine.nom,
            "quantite_ressource": self.quantite_ressource.json(),
            "duree": self.duree,
            "etape_suivante": self.etape_suivante.nom if self.etape_suivante else None
        }

    def __str__(self):
        return self.nom


class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)

    def json(self):
        return {
            "nom": self.nom,
            "premiere_etape": self.premiere_etape.nom
        }


class Stock(models.Model):
    objet = models.ForeignKey(Objet, on_delete=models.CASCADE)
    nombre = models.IntegerField()
    usine = models.ForeignKey(Usine, on_delete=models.CASCADE)

    def costs(self):
        return self.objet.prix * self.nombre

    def json(self):
        return {
            "objet": self.objet.nom,
            "nombre": self.nombre
        }
