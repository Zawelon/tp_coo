from django.contrib import admin
from django.urls import path
from high_level import views

urlpatterns = [
    # Admin URL
    path("admin/", admin.site.urls),
    # JSON views for individual models
    path("Ville/<int:pk>", views.VilleJsonDetailView.as_view(), name="Ville"),
    path("Usine/<int:pk>", views.UsineJsonDetailView.as_view(), name="Usine"),
    path("api/<int:pk>", views.UsineApiView.as_view(), name="Usine-Api"),
    path(
        "Produit/<int:pk>",
        views.ProduitJsonDetailView.as_view(),
        name="Produit",
    ),
    path("Local/<int:pk>", views.LocalJsonDetailView.as_view(), name="Local"),
    path(
        "Machine/<int:pk>",
        views.MachineJsonDetailView.as_view(),
        name="Machine",
    ),
    path("Objet/<int:pk>", views.ObjetJsonDetailView.as_view(), name="Objet"),
    path(
        "SiegeSocial/<int:pk>",
        views.SiegeSocialJsonDetailView.as_view(),
        name="SiegeSocial",
    ),
    path(
        "Ressource/<int:pk>",
        views.RessourceJsonDetailView.as_view(),
        name="Ressource",
    ),
    path(
        "QuantiteRessource/<int:pk>",
        views.QuantiteRessourceJsonDetailView.as_view(),
        name="QuantiteRessource",
    ),
    path("Etape/<int:pk>", views.EtapeJsonDetailView.as_view(), name="Etape"),
    path("Stock/<int:pk>", views.StockJsonDetailView.as_view(), name="Stock"),
]
