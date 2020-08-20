from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
# Create your views here.

def home(request):
	 #Si l'id de l'article est supérieur à 100 alors on considère que le page est introuvble 
	#if id_article > 100:
	#	raise Http404

	return HttpResponse("Bonjour")


def list_article(request):
	return redirect('redirection') # Redirection est le nom d'une URL défini dans le fichier urls.py


def view_redirection(request):
	return HttpResponse("Vous avez été redirigé")


def date(request):
	date = datetime.now()
	return render(requet, 'blog/date.html', locals())

def addition(request, nombre1, nombre2):
	somme = nombre1 + nombre2
	return render(request, 'blog/addition.html', locals())