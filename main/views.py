from django.shortcuts import render
from django.views.generic import ListView
from main.models import *

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

class StanicaList(ListView):
    model = Meteoroloska_stanica

class Zupanija_ProvincijaList(ListView):
    model = Zupanija_Provincija
    
class GradList(ListView):
    model = Grad

class PrognozaList(ListView):
    model = Podaci
        