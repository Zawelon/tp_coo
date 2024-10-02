from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)  # nom de la ville
    code_postal = models.IntegerField(default=0)  # code postal de la ville
    prix_par_m2 = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # prix par metre carre

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "code_postal": self.code_postal,
            "prix_par_m2": str(self.prix_par_m2),
        }


class Local(models.Model):
    nom = models.CharField(max_length=100)  # nom du local
    ville = models.ForeignKey(
        Ville, on_delete=models.CASCADE
    )  # ville ou se situe le local
    surface = models.DecimalField(max_digits=10, decimal_places=2)  # surface du local

    class Meta:
        abstract = True

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "ville": self.ville.nom,
            "surface": str(self.surface),
        }


class SiegeSocial(Local):
    pass  # siege social est un type de local


class Machine(models.Model):
    nom = models.CharField(max_length=100)  # nom de la machine
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # prix de la machine
    n_serie = models.CharField(max_length=100)  # numero de serie de la machine

    def costs(self):
        return self.prix  # le cout d'une machine est son prix

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "prix": str(self.prix),
            "n_serie": self.n_serie,
        }


class Usine(Local):
    machines = models.ManyToManyField(Machine)  # les machines presentes dans l'usine

    def costs(self):
        area_cost = self.surface * self.ville.prix_par_m2  # cout de la surface
        machines_cost = sum(
            machine.costs() for machine in self.machines.all()
        )  # cout des machines
        stock_cost = sum(
            stock.costs() for stock in self.stock_set.all()
        )  # cout du stock
        return area_cost + machines_cost + stock_cost  # cout total de l'usine

    def json(self):
        return {
            "nom": self.nom,
            "surface": str(self.surface),
            "ville": self.ville.nom,
            "machines": [machine.nom for machine in self.machines.all()],
            "stock": [stock.json() for stock in self.stock_set.all()],
        }

    def __str__(self):
        return self.nom


class Objet(models.Model):
    nom = models.CharField(max_length=100)  # nom de l'objet
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # prix de l'objet

    def json(self):
        return {
            "nom": self.nom,
            "prix": str(self.prix),
        }

    def __str__(self):
        return self.nom


class Ressource(Objet):
    pass  # une ressource est un type d'objet


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)  # quantite de la ressource

    def costs(self):
        return (
            self.quantite * self.ressource.prix
        )  # cout total de la quantite de ressource

    def __str__(self):
        return f"{self.quantite} de {self.ressource.nom}"


class Etape(models.Model):
    nom = models.CharField(max_length=100)  # nom de l'etape
    machine = models.ForeignKey(
        Machine, on_delete=models.CASCADE
    )  # machine utilisee pour l'etape
    quantite_ressource = models.ForeignKey(
        QuantiteRessource, on_delete=models.CASCADE
    )  # quantite de ressource utilisee
    duree = models.IntegerField()  # duree de l'etape en minutes
    etape_suivante = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="precedente",
    )  # etape suivante dans le processus

    def json(self):
        return {
            "nom": self.nom,
            "machine": self.machine.nom,
            "quantite_ressource": self.quantite_ressource.json(),
            "duree": self.duree,
            "etape_suivante": self.etape_suivante.nom if self.etape_suivante else None,
        }

    def __str__(self):
        return self.nom


class Produit(Objet):
    premiere_etape = models.ForeignKey(
        Etape, on_delete=models.CASCADE
    )  # premiere etape de production

    def json(self):
        return {
            "nom": self.nom,
            "premiere_etape": self.premiere_etape.nom,
        }


class Stock(models.Model):
    objet = models.ForeignKey(Objet, on_delete=models.CASCADE)  # objet en stock
    nombre = models.IntegerField()  # quantite en stock
    usine = models.ForeignKey(
        Usine, on_delete=models.CASCADE
    )  # usine ou se trouve le stock

    def costs(self):
        return self.objet.prix * self.nombre  # cout total du stock

    def json(self):
        return {
            "objet": self.objet.nom,
            "nombre": self.nombre,
        }
