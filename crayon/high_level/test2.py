from django.test import TestCase
from high_level.models import Ville, Usine, Machine, Stock, Objet


class UsineCostTest(TestCase):
    def setUp(self):
        # 创建一个城市 Ville Labège，价格为 2,000 €/m²
        self.ville = Ville.objects.create(
            nom="Labège", code_postal=31444, prix_par_m2=2000
        )

        # 创建一个 Usine，面积为 50 m²
        self.usine = Usine.objects.create(
            nom="Usine Test", ville=self.ville, surface=50
        )

        # 创建两台机器：一台价格为 1,000 €，另一台价格为 2,000 €
        self.machine1 = Machine.objects.create(nom="Machine 1", prix=1000, n_serie="M1")
        self.machine2 = Machine.objects.create(nom="Machine 2", prix=2000, n_serie="M2")

        # 将两台机器添加到 Usine
        self.usine.machines.add(self.machine1, self.machine2)

        # 创建资源 "bois" 和 "minerai" 作为 Objet
        self.bois = Objet.objects.create(nom="Bois", prix=10)
        self.minerai = Objet.objects.create(nom="Minerai", prix=15)

        # 创建 Stock 条目：1,000 kg 木材和 50 米矿石
        Stock.objects.create(
            objet=self.bois, nombre=1000, usine=self.usine
        )  # 1,000 kg 木材
        Stock.objects.create(
            objet=self.minerai, nombre=50, usine=self.usine
        )  # 50 米矿石

    def test_usine_costs(self):
        # 验证 Usine 的总成本是否等于 113,750 €
        expected_cost = 113750
        usine_cost = self.usine.costs()

        self.assertEqual(usine_cost, expected_cost)
