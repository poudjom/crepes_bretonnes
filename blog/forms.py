from django import forms
from .models import *

class CategorieForms(forms.ModelForm):
    #nom = forms.CharField(max_length = 30)
    class Meta:
        model = Categorie
        fields =  '__all__'


class ArticleForm(forms.Form):
    titre = forms.CharField(max_length = 100)
    slug = forms.CharField()
    auteur = forms.CharField(max_length = 100)
    contenu = forms.CharField(widget = forms.Textarea)
    date = forms.CharField(widget = forms.DateInput)
    
    # pour controller la valeur saisir dans le champs titre
    # Ici nous renvoyons une erreur si le le titre de l'article contient le mot MRC
    def clean_titre(self):
        titre = self.cleaned_data['titre']
        if 'MRC' in titre:
            raise forms.ValidationError("La titre ne doit pas contenir le caractère a")
        
        return titre
    
    #pour controle la valeur saisie dans deux champs.
    # Ici nous renvoyons une erreur de validation du formulaire si le nom de l'auteur apparait dans le contenu de l'article
    def clean(self):
        champs = super(ArticleForm, self).clean()
        auteur = champs.get('auteur')
        contenu = champs.get('contenu')
        if auteur and contenu:
            if auteur in contenu:
                # Pour afficher le message d'erreur au debut ou à la fin de la page, on utilise l'instruction ci-dessous
                #raise forms.ValidationError("Le nom de l'auteur ne peut pas apparaitre dans le contenu de l'article")
                
                #Pour afficher le message sur le champs qui n'a pas été validé, on procède comme ci-dessous
                self.add_error('contenu', 'Le nom de l\'auteur ne doit pas apparaitre dans le message')
            
        #on précise le champs du formulaire où sera renvoyé le message d'erreur
        return champs
    
    
# génération du formulaire à partir du modele directement
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'
        
        # On peut aussi lister les champs qui seront affichés dans le formulaire comme ci-dessous
        #fields('matricule', 'nom')
        
        # Ou on peut aussi choisir d'exclure ceux qui ne seront pas affiché dan sle formulaire
        #exclude('prenom', 'nom')
        
        
        
        
              