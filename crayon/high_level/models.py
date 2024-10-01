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
    def costs(self):
        return self.prix
    def __str__(self):
        return self.nom


# 工厂模型 (Usine)
class Usine(Local):
    machines = models.ManyToManyField(Machine)

    def costs(self):
        # 计算工厂的面积成本
        area_cost = self.surface * self.ville.prix_par_m2

        # 计算所有机器的成本
        machines_cost = sum(machine.costs() for machine in self.machines.all())

        # 计算库存中的资源成本
        stock_cost = sum(stock.costs() for stock in self.stock_set.all())

        return area_cost + machines_cost + stock_cost

    def get_usine_stock(self):
        """
        获取工厂当前的库存信息。
        返回一个字典，键为资源名称，值为库存数量。
        """
        return {stock.objet.nom: stock.nombre for stock in self.stock_set.all()}

    def get_required_ressources(self, produit, quantite=1):
        """
        计算生产指定数量的产品所需的所有资源。
        返回一个字典，键为资源名称，值为所需数量。
        """
        ressources = {}
        etape = produit.premiere_etape
        while etape:
            ressource_nom = etape.quantite_ressource.ressource.nom
            ressource_quantite = etape.quantite_ressource.quantite * quantite
            if ressource_nom in ressources:
                ressources[ressource_nom] += ressource_quantite
            else:
                ressources[ressource_nom] = ressource_quantite
            etape = etape.etape_suivante
        return ressources

    def check_and_buy_stock(self, produit, quantite=1):
        """
        检查工厂库存是否足够生产产品，如果不足则自动购买。
        """
        stock = self.get_usine_stock()
        required = self.get_required_ressources(produit, quantite)

        for ressource, quantite_needed in required.items():
            quantite_in_stock = stock.get(ressource, 0)
            if quantite_in_stock < quantite_needed:
                # 如果库存不足，补充差额
                self.acheter_ressource(ressource, quantite_needed - quantite_in_stock)

    def acheter_ressource(self, ressource_nom, quantite):
        """
        自动购买资源，更新库存。
        """
        # 查找资源对象
        ressource = Objet.objects.get(nom=ressource_nom)

        # 检查该资源是否已经在库存中
        stock, created = Stock.objects.get_or_create(objet=ressource, usine=self)

        # 更新库存数量
        stock.nombre += quantite
        stock.save()

    def approvisionnement_automatique(self, produit, quantite=1):
        """
        自动为工厂补充资源，以生产指定数量的产品。
        """
        print(f"Checking stock for producing {quantite} of {produit.nom}")
        self.check_and_buy_stock(produit, quantite)

# 资源模型 (Class Objet)
class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom


# 资源模型 (Ressource)
class Ressource(Objet):
    pass


# 资源数量模型 (QuantiteRessource)
class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)

    def costs(self):
        # 返回资源的价格乘以数量
        return self.quantite * self.ressource.prix

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
class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)


# 库存模型 (Stock)
class Stock(models.Model):
    objet = models.ForeignKey(Objet, on_delete=models.CASCADE)
    nombre = models.IntegerField()
    usine = models.ForeignKey(Usine, on_delete=models.CASCADE)

    def costs(self):
        # 计算库存资源的成本
        return self.objet.prix * self.nombre
