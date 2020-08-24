from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length = 100)
    auteur = models.CharField(max_length = 100)
    contenu = models.TextField(null = True)
    slug = models.SlugField(max_length=100, default="")
    date = models.DateField(default = timezone.now, verbose_name="Date publication")
    nombrevues = models.IntegerField(default = 0, verbose_name = "Nombre de lecture")
    categorie = models.ForeignKey("categorie", on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Article"
        ordering = ['date']    
        
        
    def __str__(self):
        return self.titre



class Categorie(models.Model):
    nom = models.CharField(max_length = 30)
     
    class Meta:
        verbose_name  = "Catégorie"
         
    def __str__(self):
        return self.nom

    
class Personnel(models.Model):
    matricule = models.CharField(max_length = 5)
    prenom = models.CharField(max_length = 50)
    nom = models.CharField(max_length = 50)
    
    class Meta:
        verbose_name = 'Personnel'
        
    def __str__(self):
        return self.nom