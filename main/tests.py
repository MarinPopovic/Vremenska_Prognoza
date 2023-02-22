from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from main.models import *
from main.views import *
from django.contrib.auth.models import User

# Create your tests here.
#Naredba: ./manage.py test main.tests

#Testiranje urls.py
class TestUrls(SimpleTestCase):
    #Testiranje URL-ova  
    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        print("Rezultat testiranja homepage URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, homepage)
        
    def test_registration_url_is_resolved(self):
        url = reverse('registration')
        print("Rezultat testiranja registration URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, registration)
    
    def test_stanice_url_is_resolved(self):
        url = reverse('stanice')
        print("Rezultat testiranja stanice URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func.view_class, StanicaList)
        
    def test_zupanije_url_is_resolved(self):
        url = reverse('zupanije')
        print("Rezultat testiranja zupanije URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func.view_class, Zupanija_ProvincijaList)    
        
    def test_gradovi_url_is_resolved(self):
        url = reverse('gradovi')
        print("Rezultat testiranja gradovi URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func.view_class, GradList)
        
    def test_prognoza_url_is_resolved(self):
        url = reverse('prognoza')
        print("Rezultat testiranja prognoza URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func.view_class, PrognozaList)
        
    def test_prognoza_url_is_resolved(self):
        url = reverse('upload')
        print("Rezultat testiranja upload URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, upload)
    #Testiranje update URL-ova      
    def test_update_stanica_url_is_resolved(self):
        url = reverse('update-stanica', kwargs={'stanica_id': 1}) #kwargs={'stanica_id': 1} -> an ID is passed to URL
        print("Rezultat testiranja update-stanica URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, update_stanica)
    
    def test_update_zupanija_url_is_resolved(self):
        url = reverse('update-zupanija', kwargs={'zupanija_id': 1})
        print("Rezultat testiranja update-zupanija URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, update_zupanija)
    
    def test_update_grad_url_is_resolved(self):
        url = reverse('update-grad', kwargs={'grad_id': 1})
        print("Rezultat testiranja update-grad URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, update_grad)
        
    def test_update_podaci_url_is_resolved(self):
        url = reverse('update-podaci', kwargs={'podaci_id': 1})
        print("Rezultat testiranja update-podaci URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, update_podaci)
    #Testiranje delete URL-ova   
    def test_delete_stanica_url_is_resolved(self):
        url = reverse('delete-stanica', kwargs={'stanica_id': 1})
        print("Rezultat testiranja delete-stanica URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, delete_stanica)
        
    def test_delete_zupanija_url_is_resolved(self):
        url = reverse('delete-zupanija', kwargs={'zupanija_id': 1})
        print("Rezultat testiranja delete-zupanija URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, delete_zupanija)
        
    def test_delete_grad_url_is_resolved(self):
        url = reverse('delete-grad', kwargs={'grad_id': 1})
        print("Rezultat testiranja delete-grad URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, delete_grad)
        
    def test_delete_podaci_url_is_resolved(self):
        url = reverse('delete-podaci', kwargs={'podaci_id': 1})
        print("Rezultat testiranja delete-podaci URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, delete_podaci)
    #Testiranje search URL-ova  
    def test_search_stanice_url_is_resolved(self):
        url = reverse('search-stanice')
        print("Rezultat testiranja search-stanice URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, search_stanice)
        
    def test_search_zupanija_url_is_resolved(self):
        url = reverse('search-zupanija')
        print("Rezultat testiranja search-stanice URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, search_zupanija)
        
    def test_search_grad_url_is_resolved(self):
        url = reverse('search-grad')
        print("Rezultat testiranja search-stanice URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, search_grad)
        
    def test_search_podaci_date_url_is_resolved(self):
        url = reverse('search-podaci-date')
        print("Rezultat testiranja search-stanice URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, search_podaci_date)
        
    def test_search_podaci_grad_url_is_resolved(self):
        url = reverse('search-podaci-grad')
        print("Rezultat testiranja search-stanice URL-a: ",resolve(url))
        self.assertEquals(resolve(url).func, search_podaci_grad)

#Testirnaje modela        
class Testmodels(TestCase):
    def setUp(self):
        self.stanica1 = Meteoroloska_stanica.objects.create(
            Sifra_stanice="ABC12",
            Naziv_stanice="Stanica 1"
        )
        self.zupanija1 = Zupanija_Provincija.objects.create(
            Sifra_zupanije_provincije="123456",
            Ime_Zupanije_provincije="Zupanija 1",
            Stanica=self.stanica1
        )
        self.grad1 = Grad.objects.create(
            Postanski_broj="12345",
            Naziv_grada="Grad 1",
            Zupanija_Provincija_County=self.zupanija1
        )
        self.podaci1 = Podaci.objects.create(
            Temperatura_u_C="4",
            Vjetar_brzina="1",
            Oborine="2",
            Vlaznost="80",
            Datum="2023-01-01",
            Dio_dana="Jutro",
        )
        self.podaci1.Grad_podaci.add(self.grad1)
        
    def test_stanica(self):
        self.assertEquals(self.stanica1.Sifra_stanice, "ABC12")
        self.assertEquals(self.stanica1.Naziv_stanice, "Stanica 1")
        
    def test_zupanija(self):
        self.assertEquals(self.zupanija1.Sifra_zupanije_provincije, "123456")
        self.assertEquals(self.zupanija1.Ime_Zupanije_provincije, "Zupanija 1")
        self.assertEquals(self.zupanija1.Stanica, self.stanica1)
        
    def test_grad(self):
        self.assertEquals(self.grad1.Postanski_broj, "12345")
        self.assertEquals(self.grad1.Naziv_grada, "Grad 1")
        self.assertEquals(self.grad1.Zupanija_Provincija_County, self.zupanija1)
        
    def test_podaci(self):
        self.assertEquals(self.podaci1.Temperatura_u_C, "4")
        self.assertEquals(self.podaci1.Vjetar_brzina, "1")
        self.assertEquals(self.podaci1.Oborine, "2")
        self.assertEquals(self.podaci1.Vlaznost, "80")
        self.assertEquals(self.podaci1.Datum, "2023-01-01")
        self.assertEquals(self.podaci1.Dio_dana, "Jutro")
        self.assertIn(self.grad1, self.podaci1.Grad_podaci.all())
        
#Testirnaje views.py 
class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse("homepage")
        self.stanice_url = reverse("stanice")
        self.zupanije_url = reverse("zupanije")
        self.gradovi_url = reverse("gradovi")
        self.prognoza_url = reverse("prognoza")
        self.upload_url = reverse("upload")
        
        self.update_stanica_url = reverse("update-stanica", kwargs={'stanica_id': 1})
        self.update_zupanija_url = reverse("update-zupanija", kwargs={'zupanija_id': 1})
        self.update_grad_url = reverse("update-grad", kwargs={'grad_id': 1})
        self.update_podaci_url = reverse("update-podaci", kwargs={'podaci_id': 1})
        
        self.delete_stanica_url=reverse("delete-stanica", kwargs={'stanica_id': 1})
        self.delete_zupanija_url=reverse("delete-zupanija", kwargs={'zupanija_id': 1})
        self.delete_grad_url=reverse("delete-grad", kwargs={'grad_id': 1})
        self.delete_podaci_url=reverse("delete-podaci", kwargs={'podaci_id': 1})
        
        self.search_stanice_url = reverse("search-stanice")
        self.search_zupanija_url = reverse("search-zupanija")
        self.search_grad_url = reverse("search-grad")
        self.search_podaci_date_url = reverse("search-podaci-date")
        self.search_podaci_grad_url = reverse("search-podaci-grad")
        
        self.username = "username"
        self.password = "password"
        self.user = User.objects.create_user(
           username=self.username,
           password=self.password,
       )
             
        self.stanica1 = Meteoroloska_stanica.objects.create(
            Sifra_stanice="ABC12",
            Naziv_stanice="Stanica 1"
        )
        
    def test_project_homepage_GET(self):
        response = self.client.get(self.homepage_url)
        self.assertEquals(response.status_code, 302)
        
        # Redirect to the login page
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.homepage_url}")
         
        # Login page request
        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_stanice_GET(self):
        response = self.client.get(self.stanice_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.stanice_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_zupanije_GET(self):
        response = self.client.get(self.zupanije_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.zupanije_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_gradovi_GET(self):
        response = self.client.get(self.gradovi_url)
        
        self.assertEquals(response.status_code, 302)

        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.gradovi_url}")

        response = self.client.get(login_url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_prognoza_GET(self):
        response = self.client.get(self.prognoza_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.prognoza_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_upload_GET(self):
        response = self.client.get(self.upload_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.upload_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
    #Update views-i    
    def test_project_update_stanica_GET(self):
        response = self.client.get(self.update_stanica_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.update_stanica_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_update_zupanija_GET(self):
        response = self.client.get(self.update_zupanija_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.update_zupanija_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_update_grad_GET(self):
        response = self.client.get(self.update_grad_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.update_grad_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_update_podaci_GET(self):
        response = self.client.get(self.update_podaci_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.update_podaci_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
    #Delete views-i 
    def test_project_delete_stanica_GET(self):
        response = self.client.get(self.delete_stanica_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.delete_stanica_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_delete_zupanija_GET(self):
        response = self.client.get(self.delete_zupanija_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.delete_zupanija_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_delete_grad_GET(self):
        response = self.client.get(self.delete_grad_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.delete_grad_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_project_delete_podaci_GET(self):
        response = self.client.get(self.delete_podaci_url)
        self.assertEquals(response.status_code, 302)
        
        login_url = reverse("login")
        self.assertRedirects(response, f"{login_url}?next={self.delete_podaci_url}")

        response = self.client.get(login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
    #search views-i    
    def test_project_search_stanice_GET(self):
        client = Client()

        response = client.get(self.search_stanice_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_stanice.html')
        
    def test_project_search_zupanija_GET(self):
        client = Client()

        response = client.get(self.search_zupanija_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_zupanije.html')
        
    def test_project_search_grad_GET(self):
        client = Client()

        response = client.get(self.search_grad_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_gradovi.html')
        
    def test_project_search_podaci_date_GET(self):
        client = Client()

        response = client.get(self.search_podaci_date_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_podaci_date.html')
        
    def test_project_search_podaci_grad_GET(self):
        client = Client()

        response = client.get(self.search_podaci_grad_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_podaci_grad.html')
    