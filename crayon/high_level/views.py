from django.shortcuts import render
from high_level.models import Usine, Produit

def produire_produit(request, produit_id, quantite):
    # 获取 Usine 和 Produit 对象
    usine = Usine.objects.first()  # 假设只有一个工厂
    produit = Produit.objects.get(id=produit_id)

    # 自动为生产补充库存
    usine.approvisionnement_automatique(produit, quantite)

    # 在此处调用生产逻辑（如有）
    # manage_production(usine, produit, quantite)

    return render(request, 'production.html', {'usine': usine, 'produit': produit, 'quantite': quantite})
# Create your views here.
