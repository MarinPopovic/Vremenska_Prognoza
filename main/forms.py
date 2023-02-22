from django.forms import ModelForm
from django import forms
from .models import *

class UploadFormStanica(ModelForm):
    
    class Meta:
        model = Meteoroloska_stanica
        fields = ('Sifra_stanice', 'Naziv_stanice')
        
        widgets = {
            'Sifra_stanice':forms.TextInput(attrs={'placeholder':'Sifra stanice'}),
            'Naziv_stanice':forms.TextInput(attrs={'placeholder':'Naziv stanice'})
        }
        
class UploadFormZupanija(ModelForm):
    class Meta:
        model = Zupanija_Provincija
        fields = ('Sifra_zupanije_provincije', 'Ime_Zupanije_provincije', 'Stanica')
        
        widgets = {
            'Sifra_zupanije_provincije':forms.TextInput(attrs={'placeholder': 'Sifra zupanije'}),
            'Ime_Zupanije_provincije':forms.TextInput(attrs={'placeholder': 'Ime zupanije'}),
        }
        
class UploadFormGrad(ModelForm):
    class Meta:
        model = Grad
        fields = ('Postanski_broj', 'Naziv_grada', 'Zupanija_Provincija_County')
        
        widgets = {
            'Postanski_broj':forms.TextInput(attrs={'placeholder':'Postanski broj'}),
            'Naziv_grada':forms.TextInput(attrs={'placeholder':'Naziv grada'}),
        }
        
        
class UploadFormPodaci(ModelForm):
    class Meta:
        model = Podaci
        fields = "__all__"
        
        widgets = {
            'Temperatura_u_C':forms.NumberInput(attrs={'placeholder':'Temperatura (C)'}),
            'Vjetar_brzina':forms.NumberInput(attrs={'placeholder':'Brzina vjetra (km/h)'}),
            'Oborine':forms.NumberInput(attrs={'placeholder':'Oborine (mm)'}),
            'Vlaznost':forms.NumberInput(attrs={'placeholder':'Vlaznost (%)'}),
            'Datum':forms.SelectDateWidget()
        }