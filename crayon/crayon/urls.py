from django.contrib import admin
from django.urls import path
from high_level import views

urlpatterns = [
  
    path("admin/", admin.site.urls),

    path('produire/<int:produit_id>/<int:quantite>/', views.produire_produit, name='produire_produit'),


    path('ville/<int:pk>/json/', views.VilleJsonDetailView.as_view(), name='ville_json'),
    path('usine/<int:pk>/json/', views.UsineJsonDetailView.as_view(), name='usine_json'),
    path('produit/<int:pk>/json/', views.ProduitJsonDetailView.as_view(), name='produit_json'),
]