from django.urls import path
from . import views
from main.views import *

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registration, name='registration'),
    path('logout/', views.LogoutView, name='logout'),
    
    path('stanice', StanicaList.as_view(), name='stanice'),
    path('zupanije', Zupanija_ProvincijaList.as_view(), name='zupanije'),
    path('gradovi', GradList.as_view(), name='gradovi'),
    path('prognoza', PrognozaList.as_view(), name='prognoza'),
    
    path('upload', views.upload, name='upload'),
    
    path('delete_stanica/<int:stanica_id>/', views.delete_stanica, name='delete-stanica'),
    path('delete_zupanija/<int:zupanija_id>/', views.delete_zupanija, name='delete-zupanija'),
    path('delete_grad/<int:grad_id>/', views.delete_grad, name='delete-grad'),
    path('delete_podaci/<int:podaci_id>/', views.delete_podaci, name='delete-podaci'),
    
    path('update_stanica/<int:stanica_id>/', views.update_stanica, name='update-stanica'),
    path('update_zupanija/<int:zupanija_id>/', views.update_zupanija, name='update-zupanija'),
    path('update_grad/<int:grad_id>/', views.update_grad, name='update-grad'),
    path('update_podaci/<int:podaci_id>/', views.update_podaci, name='update-podaci'),
    
    path('search_stanice', views.search_stanice, name='search-stanice'),
    path('search_zupanija', views.search_zupanija, name='search-zupanija'),
    path('search_grad', views.search_grad, name='search-grad'),
    path('search_podaci_date', views.search_podaci_date, name='search-podaci-date'),
    path('search_podaci_grad', views.search_podaci_grad, name='search-podaci-grad'),
]