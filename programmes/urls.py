from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('programmes/', views.liste_programmes, name='liste_programmes'),
    path('programme/<int:programme_id>/', views.detail_programme, name='detail_programme'),

    path('creer_programme/', views.creer_programme, name='creer_programme'),
    path('login_sous_admin/', views.login_sous_admin, name='login_sous_admin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ajouter_activite/', views.ajouter_activite, name='ajouter_activite'),
    path('modifier_activite/<int:activite_id>/', views.modifier_activite, name='modifier_activite'),
    path('supprimer_activite/<int:activite_id>/', views.supprimer_activite, name='supprimer_activite'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]
