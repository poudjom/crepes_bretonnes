from django.contrib import admin
from .models import *
from django.utils.text import Truncator
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'apercu_contenu', 'auteur', 'date', 'nombrevues')
    list_filter = ('categorie', 'auteur')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields  = ('titre', 'contenu')
    
    # préremplissement automatique du champs slug avec la valeur saisie dans le champs titre
    prepopulated_fields = {'slug': ('titre', ), } 
    
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            # la propriété classe permet de regrouper un groupe de champs afin de les affichier ou les masquer au besoin
            #'classes': ['collapse',],
            'fields': ('titre', 'slug', 'auteur', 'categorie')
            }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
            #'classes': ['collapse',],
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('contenu', )
            }),
        )
    
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'
    
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
    