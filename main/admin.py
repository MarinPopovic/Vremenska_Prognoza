from django.contrib import admin

from main.models import *

models_list = [Zupanija_Provincija, Grad, Podaci, Meteoroloska_stanica]

## Register your models here.
admin.site.register(models_list)
