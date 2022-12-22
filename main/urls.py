from django.urls import path
from . import views
from main.views import *


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('stanice', StanicaList.as_view()),
    path('zupanije', Zupanija_ProvincijaList.as_view()),
    path('gradovi', GradList.as_view()),
    path('prognoza', PrognozaList.as_view()),
]