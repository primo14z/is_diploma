from django.conf.urls import url, include
from django.contrib import admin
from . import views


app_name='KmetApp'

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^prijava/', views.prijava , name='prijava'),
    url(r'^logIn/', views.logIn , name='logIn'),
    url(r'^logOut/', views.logOut , name='logOut'),
    url(r'^registracija/', views.registracija , name='registracija'),
    url(r'^reg/', views.reg , name='reg'),
    url(r'^oglas/', views.oglas , name='oglas'),
    url(r'^oddaja_O/', views.oddaja_O , name='oddaja_O'),
    url(r'^iskanje_O/', views.iskanje_O , name='iskanje_O'),
    url(r'^oglas_O/', views.oglas_O , name='oglas_O'),
    url(r'^narocilo_O/', views.narocilo_O , name='narocilo_O'),
   	url(r'^oglas_M/', views.oglas_M , name='oglas_M'),
   	url(r'^oglas_Edit/', views.oglas_Edit , name='oglas_Edit'),
   	url(r'^oglas_E/', views.oglas_E , name='oglas_E'),
    url(r'^narocilo/', views.narocilo , name='narocilo'),
    url(r'^narocilo_IO/', views.narocilo_IO , name='narocilo_IO'),
    url(r'^narocilo_E/', views.narocilo_E , name='narocilo_E'),
	url(r'^narocila_N/', views.narocila_N , name='narocila_N'),
	url(r'^narocila_M/', views.narocila_M , name='narocila_M'),
	
	url(r'^obdelaj_N/', views.obdelaj_N , name='obdelaj_N'),
	url(r'^zakljuci_O/', views.zakljuci_O , name='zakljuci_O'),
	url(r'^kosarica/', views.kosarica , name='kosarica'),
	url(r'^oddaja_K/', views.oddaja_K , name='oddaja_K'),
	url(r'^kosarica_O/', views.kosarica_O , name='kosarica_O'),
	url(r'^iskanje_K/', views.iskanje_K , name='iskanje_K'),
	url(r'^kosarica_E/', views.kosarica_E , name='kosarica_E'),
	url(r'^kosarica_M/', views.kosarica_M , name='kosarica_M'),
	url(r'^narocila_K_N/', views.narocila_K_N , name='narocila_K_N'),
	url(r'^narocila_K_NE/', views.narocila_K_NE , name='narocila_K_NE'),
	url(r'^narocilo_K_O/', views.narocilo_K_O , name='narocilo_K_O'),
	url(r'^narocila_K_M/', views.narocila_K_M , name='narocila_K_M'),
	url(r'^obdelaj_K_N/', views.obdelaj_K_N , name='obdelaj_K_N'),
	url(r'^narocilo_Obdelano/', views.narocilo_Obdelano , name='narocilo_Obdelano'),
	url(r'^narocila_K_Moja/', views.narocila_K_Moja , name='narocila_K_Moja'),
	url(r'^narocila_K_O/', views.narocila_K_O , name='narocila_K_O'),
	url(r'^narocila_K_obdelana/' , views.narocila_K_obdelana , name='narocila_K_obdelana'),
	url(r'^Edit/', views.Edit, name='Edit'),
	url(r'^popraviPodatke/' , views.popraviPodatke , name='popraviPodatke'),
	url(r'^oglas_view/' , views.oglas_view , name='oglas_view')
]

