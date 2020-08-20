from django.urls import path
from . import views

urlpatterns = [
    path('acceuil', views.home),
    path('list_article', views.list_article, name = 'listearticle'),
    path('redirection', views.view_redirection, name = 'redirection'),
    path('date', views.date, name = 'date'),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition, name = 'addition'),
]