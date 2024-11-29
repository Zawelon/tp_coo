from django.contrib import admin
from django.urls import path
from high_level import views

urlpatterns = [
    # Admin URL
    path("admin/", admin.site.urls),
    # JSON views for individual models
    path(
        "ville/<int:pk>/json/", views.VilleJsonDetailView.as_view(), name="ville_json"
    ),
    path(
        "usine/<int:pk>/json/", views.UsineJsonDetailView.as_view(), name="usine_json"
    ),
    path(
        "produit/<int:pk>/json/",
        views.ProduitJsonDetailView.as_view(),
        name="produit_json",
    ),
    path(
        "local/<int:pk>/json/", views.LocalJsonDetailView.as_view(), name="local_json"
    ),
    path(
        "machine/<int:pk>/json/",
        views.MachineJsonDetailView.as_view(),
        name="machine_json",
    ),
    path(
        "objet/<int:pk>/json/", views.ObjetJsonDetailView.as_view(), name="objet_json"
    ),
    path(
        "siege_social/<int:pk>/json/",
        views.SiegeSocialJsonDetailView.as_view(),
        name="siege_social_json",
    ),
    path(
        "ressource/<int:pk>/json/",
        views.RessourceJsonDetailView.as_view(),
        name="ressource_json",
    ),
    path(
        "quantite_ressource/<int:pk>/json/",
        views.QuantiteRessourceJsonDetailView.as_view(),
        name="quantite_ressource_json",
    ),
    path(
        "etape/<int:pk>/json/", views.EtapeJsonDetailView.as_view(), name="etape_json"
    ),
    path(
        "stock/<int:pk>/json/", views.StockJsonDetailView.as_view(), name="stock_json"
    ),
    """
    # Extended JSON views for models and their relations (for C++ requirements)
    path("api/ville/<int:pk>/", views.VilleApiView.as_view(), name="api_ville"),
    path("api/local/<int:pk>/", views.LocalApiView.as_view(), name="api_local"),
    path("api/usine/<int:pk>/", views.UsineApiView.as_view(), name="api_usine"),
    path("api/machine/<int:pk>/", views.MachineApiView.as_view(), name="api_machine"),
    path("api/objet/<int:pk>/", views.ObjetApiView.as_view(), name="api_objet"),
    path(
        "api/siege_social/<int:pk>/",
        views.SiegeSocialApiView.as_view(),
        name="api_siege_social",
    ),
    path(
        "api/ressource/<int:pk>/",
        views.RessourceApiView.as_view(),
        name="api_ressource",
    ),
    path(
        "api/quantite_ressource/<int:pk>/",
        views.QuantiteRessourceApiView.as_view(),
        name="api_quantite_ressource",
    ),
    path("api/etape/<int:pk>/", views.EtapeApiView.as_view(), name="api_etape"),
    path("api/produit/<int:pk>/", views.ProduitApiView.as_view(), name="api_produit"),
    path("api/stock/<int:pk>/", views.StockApiView.as_view(), name="api_stock"),
    """,
]
