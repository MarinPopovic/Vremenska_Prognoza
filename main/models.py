from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
    
class Meteoroloska_stanica(models.Model): #Napomena: postavljeno je pravilo da svaka zupanija/provincija ima jednu met. stanicu i obrnuto
    Sifra_stanice=models.CharField(max_length=5)
    Naziv_stanice=models.CharField(max_length=25)   
    
    class Meta:
         ordering = ['Naziv_stanice']
    
    def __str__(self):
        return self.Naziv_stanice
    
class Zupanija_Provincija(models.Model):
    Sifra_zupanije_provincije=models.CharField('Sifra zupanije/provincije', max_length=5)
    Ime_Zupanije_provincije=models.CharField('Ime zupanije/provincije', max_length=30)
    Stanica=models.OneToOneField(Meteoroloska_stanica, on_delete=models.CASCADE)
    
    class Meta:
         ordering = ['Ime_Zupanije_provincije']
    
    def __str__(self):
        return self.Ime_Zupanije_provincije #Prikazat i sifru i ime
           
class Grad(models.Model):
    Postanski_broj=models.IntegerField(validators=[
            MaxValueValidator(99999),
            MinValueValidator(10000)
        ])
    Naziv_grada=models.CharField(max_length=30)
    Zupanija_Provincija_County=models.ForeignKey(Zupanija_Provincija, on_delete=models.CASCADE)
    
    class Meta:
         ordering = ['Naziv_grada']
    
    def __str__(self):
        return f'{self.Naziv_grada}'
    
class Podaci(models.Model):
    Grad_podaci=models.ManyToManyField(Grad) #promijeniti ime Naziv_grada u Grad_podaci
    Temperatura_u_C=models.FloatField() #Primjer podatka: 5°C
    Vjetar_brzina=models.IntegerField() #Primjer podatka: 5 km/h
    Oborine=models.FloatField() #Primjer podatka: 5.5°C
    Vlaznost=models.IntegerField(validators=[ #Primjer podatka: 60%
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    Datum=models.DateField() #Formatirati prikaz: Ponedjeljak, 19. Prosinac
    Dio_dana=models.CharField(max_length=15, default=0) #Primjer podatka: Jutro, podne, vecer
    
    class Meta:
        ordering = ['Datum', 'Dio_dana']
    
    def __str__(self):
        return f'Prognoza za {self.Grad_podaci.all()}, {self.Datum}, {self.Dio_dana}'
    