from django.urls import path
from . import views

urlpatterns = [
    path('acceuil', views.home, name = "acceuil"),
    path('lire/<int:id>-<slug:slug>$', views.lire_article, name = 'lire'),
    path('redirection', views.view_redirection, name = 'redirection'),
    path('date', views.date, name = 'date'),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition, name = 'addition'),
    path('categorie/<int:id>', views.categorie, name = 'categorie'),
    path('article/<int:id>', views.article, name = 'article'),
    path('personnel', views.personnel, name = 'personnel')
]
