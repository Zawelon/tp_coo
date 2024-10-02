from django.test import TestCase
from high_level.models import Ville, Usine, Machine, Stock, Objet


class UsineCostTest(TestCase):
    def setUp(self):
        # creer un ville nomme "Labege", prix pour m2 est 2000 euros
        self.ville = Ville.objects.create(
            nom="Labege", code_postal=31444, prix_par_m2=2000
        )

        # creer un Usine, surface est 50 m2
        self.usine = Usine.objects.create(
            nom="Usine Test", ville=self.ville, surface=50
        )

        # creer deux machines: un prix est 1000 euros, l'autre est 2000 euros
        self.machine1 = Machine.objects.create(nom="Machine 1", prix=1000, n_serie="M1")
        self.machine2 = Machine.objects.create(nom="Machine 2", prix=2000, n_serie="M2")

        # ajouter deux machines a Usine
        self.usine.machines.add(self.machine1, self.machine2)

        # creer ressource "bois" et "minerai" comme Objet
        self.bois = Objet.objects.create(nom="Bois", prix=10)
        self.minerai = Objet.objects.create(nom="Minerai", prix=15)

        # creer Stock element: 1000 kg bois et 50 metre minerai
        Stock.objects.create(
            objet=self.bois, nombre=1000, usine=self.usine
        )  # 1000 kg bois
        Stock.objects.create(
            objet=self.minerai, nombre=50, usine=self.usine
        )  # 50 metre minerai

    def test_usine_costs(self):
        # verifier Usine cout total est egal a 113,750 euros
        expected_cost = 113750
        usine_cost = self.usine.costs()

        self.assertEqual(usine_cost, expected_cost)
