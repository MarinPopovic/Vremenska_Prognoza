from django.shortcuts import render, redirect
from django.views.generic import ListView
from main.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def homepage(request):
    return render(request, 'homepage.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            
            login(request, user)
            
            return redirect('homepage')
    else:
        form = UserCreationForm()
    
    context = {'form': form}

    return render(request, 'registration/register.html', context)

def LogoutView(request):
    logout(request)
    return redirect('login')

@login_required
def upload(request):
    if not request.user.is_superuser:
           return HttpResponse(status=403)
    
    submitted = False
    if request.method == "POST":
        form = UploadFormStanica(request.POST)
        form2 = UploadFormZupanija(request.POST)
        form3 = UploadFormGrad(request.POST)
        form4 = UploadFormPodaci(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./upload?submitted=True')
        elif form2.is_valid():
            form2.save()
            return HttpResponseRedirect('./upload?submitted=True')
        elif form3.is_valid():
            form3.save()
            return HttpResponseRedirect('./upload?submitted=True')
        elif form4.is_valid():
            form4.save()
            return HttpResponseRedirect('./upload?submitted=True')
        
    else:
     form = UploadFormStanica
     form2 = UploadFormZupanija
     form3 = UploadFormGrad
     form4 = UploadFormPodaci
     if 'submitted' in request.GET:
         submitted=True
        
    return render(request, './main/upload.html', {'form':form,'form2':form2, 'form3':form3, 'form4':form4, 'submitted':submitted})
#########################################################
@login_required
def delete_stanica(request, stanica_id):
  stanica=Meteoroloska_stanica.objects.get(id=stanica_id)
  stanica.delete()
  return redirect('stanice')

@login_required
def delete_zupanija(request, zupanija_id):
  zupanija=Zupanija_Provincija.objects.get(id=zupanija_id)
  zupanija.delete()
  return redirect('zupanije')

@login_required
def delete_grad(request, grad_id):
  grad=Grad.objects.get(id=grad_id)
  grad.delete()
  return redirect('gradovi')

@login_required
def delete_podaci(request, podaci_id):
  podaci=Podaci.objects.get(id=podaci_id)
  podaci.delete()
  return redirect('prognoza')
#########################################################
@login_required
def update_stanica(request, stanica_id):
    stanica=Meteoroloska_stanica.objects.get(pk=stanica_id)
    form = UploadFormStanica(request.POST or None, instance=stanica)
    if form.is_valid():
        form.save()
        return redirect('stanice')
    
    return render(request, 'main/update_stanica.html', {'stanica':stanica, 'form':form})

@login_required
def update_zupanija(request, zupanija_id):
    zupanija=Zupanija_Provincija.objects.get(pk=zupanija_id)
    form = UploadFormZupanija(request.POST or None, instance=zupanija)
    if form.is_valid():
        form.save()
        return redirect('zupanije')
    
    return render(request, 'main/update_zupanija.html', {'zupanija':zupanija, 'form':form})

@login_required
def update_grad(request, grad_id):
    grad=Grad.objects.get(pk=grad_id)
    form = UploadFormGrad(request.POST or None, instance=grad)
    if form.is_valid():
        form.save()
        return redirect('grad')
    
    return render(request, 'main/update_grad.html', {'grad':grad, 'form':form})

@login_required
def update_podaci(request, podaci_id):
    podaci=Podaci.objects.get(pk=podaci_id)
    form = UploadFormPodaci(request.POST or None, instance=podaci)
    if form.is_valid():
        form.save()
        return redirect('prognoza')
    
    return render(request, 'main/update_podaci.html', {'podaci':podaci, 'form':form})
#########################################################
def search_stanice(request):
   if request.method == "POST" :
     search = request.POST['search']
     stanica = Meteoroloska_stanica.objects.filter(Naziv_stanice__contains=search)
     return render(request, 'main/search_stanice.html', {'search':search, 'stanica':stanica}) 
   else: 
    return render(request, 'main/search_stanice.html', {}) 

def search_zupanija(request):
    if request.method == "POST" :
     search = request.POST['search']
     zupanija = Zupanija_Provincija.objects.filter(Ime_Zupanije_provincije__contains=search)
     return render(request, 'main/search_zupanije.html', {'search':search, 'zupanija':zupanija}) 
    else: 
     return render(request, 'main/search_zupanije.html', {}) 
 
def search_grad(request):
    if request.method == "POST" :
     search = request.POST['search']
     grad = Grad.objects.filter(Naziv_grada__contains=search)
     return render(request, 'main/search_gradovi.html', {'search':search, 'grad':grad}) 
    else: 
     return render(request, 'main/search_gradovi.html', {}) 
 
def search_podaci_date(request):
    if request.method == "POST" :
     search = request.POST['search']
     podaci_datum = Podaci.objects.filter(Datum__contains=search)
     return render(request, 'main/search_podaci_date.html', {'search':search, 'podaci_datum':podaci_datum}) 
    else: 
     return render(request, 'main/search_podaci_date.html', {}) 
 
def search_podaci_grad(request):
    if request.method == "POST":
        search = request.POST['search']
        podaci_grad = Podaci.objects.filter(Grad_podaci__in=Grad.objects.filter(Naziv_grada__contains=search))
        return render(request, 'main/search_podaci_grad.html', {'search': search, 'podaci_grad': podaci_grad})
    else:
        return render(request, 'main/search_podaci_grad.html', {})

class StanicaList(LoginRequiredMixin, ListView):
    model = Meteoroloska_stanica

class Zupanija_ProvincijaList(LoginRequiredMixin, ListView):
    model = Zupanija_Provincija
    
class GradList(LoginRequiredMixin, ListView):
    model = Grad

class PrognozaList(LoginRequiredMixin, ListView):
    model = Podaci
        