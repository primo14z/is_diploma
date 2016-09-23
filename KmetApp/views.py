from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import Http404, JsonResponse
from django.db import models
from django.contrib.auth import logout
from KmetApp.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.db.models import Q

# Create your views here.
def home(request):
	return render(request, 'index.html')

def logOut(request):
	logout(request)
	return render(request, 'index.html')

def prijava(request):
	return render(request , 'accounts/login.html')


def logIn(request):
	email = request.POST['email']
	password = request.POST['password']
	user = authenticate(email=email, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return render(request , 'index.html')
		else:
			raise Http404 ("Uporabnik ne obstaja")
	else:
		raise Http404 ("Uporabnik ")

def reg(request):
	return render(request, 'accounts/registration.html')


def registracija(request):
	email = request.POST.get('email' , '')
	password = request.POST.get('password', '')
	ime= request.POST.get('ime', '')
	priimek=request.POST.get('priimek', '')
	naslov=request.POST.get('naslov', '')
	postna_st=request.POST.get('postna_st', '')
	kraj=request.POST.get('kraj', '')

	user=User.objects.create_user(email= email, password=password)
	user.ime=ime
	user.priimek=priimek 
	user.naslov=naslov
	user.postna_st=postna_st
	user.kraj=kraj
	user.save()
	return render(request, 'accounts/login.html')

def popraviPodatke(request):

	password = request.POST.get('password', '')
	ime= request.POST.get('ime', '')
	priimek=request.POST.get('priimek', '')
	naslov=request.POST.get('naslov', '')
	postna_st=request.POST.get('postna_st', '')
	kraj=request.POST.get('kraj', '')

	user=User.objects.get(id=request.user.id)
	user.ime=ime
	user.priimek=priimek 
	user.naslov=naslov
	user.postna_st=postna_st
	user.kraj=kraj
	user.save()
	return render(request, 'index.html')

def oglas(request):
	return render(request, 'oglas/index.html')
	
def oglas_O(request):
	return render (request, 'oglas/add.html')

def kosarica_O(request):
	return render (request, 'kosarica/add_K.html')

def oglas_M(request):
	return render(request , 'oglas/edit.html')

def narocilo(request):
	return render(request , 'narocilo/index_N.html')

def narocilo_IO(request):
	return render(request , 'narocilo/index_O.html')

def narocilo_E(request):
	return render(request , 'narocilo/index_M.html')

def kosarica(request):
	return render(request, 'kosarica/index.html')

def kosarica_E(request):
	return render(request , 'kosarica/edit_K.html')

def narocila_K_N(request):
	return render(request ,'narocilo_K/index_N.html')

def narocila_K_M(request):
	return render(request , 'narocilo_K/index_M.html')

def narocila_K_O(request):
	return render(request , 'narocilo_K/index_O.html')
def Edit(request):
	return render(request , 'accounts/Edit.html')



def oddaja_K(request): #oddaja košarice
	ime_K = request.POST.get('ime_K' , '')
	cena_K = request.POST.get('cena_K', 1)
	kolicina_K = request.POST.get('kolicina_K', 1)
	opis_K = request.POST.get('opis_K' , '')
	stevilo_K = request.POST.get('stevilo_K', 1)
	prodajalec_K=request.user

	if prodajalec_K.is_authenticated:
		kosarica=Kosarica.objects.create(ime_K=ime_K, cena_K=cena_K, kolicina_K=kolicina_K, opis_K=opis_K, prodajalec_K=prodajalec_K, stevilo_K = stevilo_K)
	else:
		raise Http404 ("Uporabnik ne obstaja")
	return render(request, 'kosarica/index.html')


def oddaja_O(request): #oddaja oglasa
	ime_O = request.POST.get('ime_O' , '')
	cena_O = request.POST.get('cena', 1)
	kolicina_O = request.POST.get('kolicina_O', 1)
	opis_O = request.POST.get('opis_O' , '')
	prodajalec_O=request.user

	if prodajalec_O.is_authenticated:
		oglas=Oglas.objects.create(ime_O=ime_O, cena_O=cena_O, kolicina_O=kolicina_O, opis_O=opis_O, prodajalec_O=prodajalec_O)
	else:
		raise Http404 ("Uporabnik ne obstaja")
	return render(request, 'oglas/index.html')

@csrf_exempt
def iskanje_O(request): #iskanje oglasa
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	print(body)
	if request.user.is_authenticated():
		iskanje = Oglas.objects.filter(ime_O__icontains= body['term']).exclude(kolicina_O =0).exclude(aktiven_O = False).exclude(prodajalec_O_id=request.user )
		print(iskanje)
	else:
		iskanje = Oglas.objects.filter(ime_O__icontains= body['term']).exclude(kolicina_O =0).exclude(aktiven_O = False)
	data = [{"ime_O": ogl.ime_O, "cena_O": ogl.cena_O, "kolicina_O": ogl.kolicina_O , "opis_O": ogl.opis_O , "oglas_id" : ogl.id } for ogl in iskanje]
	return JsonResponse({ "oglasi" : data })

@csrf_exempt
def iskanje_K(request): #iskanje košarice
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)	
	if request.user.is_authenticated():
		iskanje = Kosarica.objects.exclude(kolicina_K =0).exclude(prodajalec_K_id=request.user ).exclude(stevilo_K = 0).filter(Q(opis_K__icontains =body['term']) | Q(ime_K__icontains =body['term']))
	else:
		iskanje = Kosarica.objects.exclude(kolicina_K =0).exclude(stevilo_K = 0).filter(Q(opis_K__icontains =body['term']) | Q(ime_K__icontains =body['term']))
	data = [{"ime_K": ogl.ime_K, "cena_K": ogl.cena_K, "kolicina_K": ogl.kolicina_K, "opis_K": ogl.opis_K , "id" : ogl.id ,"stevilo_K" : ogl.stevilo_K} for ogl in iskanje]
	return JsonResponse({ "kosarice" : data })

	
@csrf_exempt
def narocilo_O(request): #oddaja naročila za oglas
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)	
	oglas = Oglas.objects.get(id = body['id'])
	if request.user.is_authenticated and (oglas.kolicina_O - body['kolicina'])>=0 :	
		cena_N_O = oglas.cena_O
		kolicina_N_O = body['kolicina']
		kupec_O_id=request.user.id
		oglas_O_id=oglas.id
		oglas.kolicina_O = oglas.kolicina_O - body['kolicina']
		oglas.save()
		narocilo=Narocilo_O.objects.create(cena_N_O=cena_N_O, kolicina_N_O=kolicina_N_O, kupec_O_id= kupec_O_id, oglas_O_id= oglas_O_id)
	else:
		raise Http404 ("Uporabnik ne obstaja")
	return JsonResponse({ "status" : "true"})

@csrf_exempt
def narocilo_K_O(request): #oddaja naročila za košarico
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	print(body)
	kosarica = Kosarica.objects.get(id = body['id'])
	print(kosarica)
	if request.user.is_authenticated and (kosarica.stevilo_K - body['stevilo_K'])>0 :	
		cena_K_N = kosarica.cena_K
		stevilo_K = body['stevilo_K']
		kupec_K_id=request.user.id
		kosarica_K_id=kosarica.id
		kosarica.stevilo_K = kosarica.stevilo_K - body['stevilo_K']
		pogostost_dostave_K =body['pogostost']
		kosarica.save()
		narocilo=Narocilo_K.objects.create(cena_K_N=cena_K_N, stevilo_K_N = stevilo_K, kupec_K_id= kupec_K_id, kosarica_K_id= kosarica_K_id , pogostost_dostave_K = pogostost_dostave_K)
	else:
		raise Http404 ("Uporabnik ne obstaja")
	return JsonResponse({ "status" : "true"})	
	




@csrf_exempt
def oglas_Edit(request): #pregled oddanih oglasov od uporabnika
	uporabnik = request.user.id	
	oglas = Oglas.objects.filter(prodajalec_O_id = uporabnik).exclude(aktiven_O = 0)
	data1 = [{"ime_O": ogl.ime_O, "cena_O": ogl.cena_O, "kolicina_O": ogl.kolicina_O , "opis_O": ogl.opis_O , "oglas_id" : ogl.id} for ogl in oglas]
	
	return JsonResponse ({"oglase" : data1})

@csrf_exempt
def oglas_E(request):# spreiminjanje že obstoječega oglasa
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)	
	oglas = Oglas.objects.get(id = body['id'])
	
	oglas.cena_O = body['cena_O']
	oglas.ime_O = body ['ime_O']
	oglas.kolicina_O = body ['kolicina_O']
	oglas.opis_O = body ['opis_O']
	oglas.save()

	return JsonResponse({ "status" : "true"})




@csrf_exempt
def narocila_N(request):#pregled oddanih naročil na obstoječi oglas, katera so neobdelana
	uporabnik = request.user.id
	
	narocilo=Narocilo_O.objects.filter(oglas_O_id__prodajalec_O_id=request.user.id).order_by('datum_N_O').filter(obdelano_N_O = 0)
	print(narocilo)
	data = [{"cena_N_O": nar.cena_N_O, "kolicina_N_O": nar.kolicina_N_O, "obdelano_N_O": nar.obdelano_N_O , "datum_N_O": nar.datum_N_O , "narocilo_id" : nar.id , "kupec_O_id" : User.objects.values("ime").get(id = nar.kupec_O_id)["ime"], "oglas_O_id" : nar.oglas_O_id , "oglas_ime" : Oglas.objects.values("ime_O").get(id = nar.oglas_O_id)["ime_O"]  } for nar in narocilo]
	
	
	return JsonResponse({"narocila" : data})




@csrf_exempt
def narocila_K_NE(request):#pregled prejetih naročil na košarico
	uporabnik = request.user.id

	
	narocilo=Narocilo_K.objects.filter(kosarica_K_id__prodajalec_K_id=request.user.id).order_by('datum_K_N').filter(obdelano_N_K = 0)
	
	data = [{"cena_K_N": nar.cena_K_N, "stevilo_K_N": nar.stevilo_K_N, "obdelano_N_K": nar.obdelano_N_K , "datum_K_N": nar.datum_K_N , "narocilo_id" : nar.id , "kupec_K_id" : User.objects.values("ime").get(id = nar.kupec_K_id)["ime"], "kosarica_K_id" : nar.kosarica_K_id , "Kosarica_ime" : Kosarica.objects.values("ime_K").get(id = nar.kosarica_K_id)["ime_K"] , "opis_K_N" : Kosarica.objects.values("opis_K").get(id = nar.kosarica_K_id)["opis_K"]  } for nar in narocilo]
	
	return JsonResponse({"narocila" : data})




@csrf_exempt
def narocila_M(request):#pregled oddanih naročil za oglas
	uporabnik = request.user.id
	
	narocilo=Narocilo_O.objects.filter(kupec_O_id= uporabnik).order_by('datum_N_O')
	print(narocilo)
	data = [{"cena_N_O": nar.cena_N_O, "kolicina_N_O": nar.kolicina_N_O, "obdelano_N_O": nar.obdelano_N_O , "datum_N_O": nar.datum_N_O , "narocilo_id" : nar.id , "kupec_O_id" : User.objects.values("ime").get(id = nar.kupec_O_id)["ime"], "oglas_O_id" : nar.oglas_O_id , "oglas_ime" : Oglas.objects.values("ime_O").get(id = nar.oglas_O_id)["ime_O"]  } for nar in narocilo]
	print(data)
	return JsonResponse({"narocila" : data})
	


@csrf_exempt
def obdelaj_N(request):#shrani v bazo kdaj je bilo naročilo obdelano in spremeni status na obdelano --> Oglas

	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)	
	
	narocilo =Narocilo_O.objects.get(id = body)
	narocilo.obdelano_N_O = True
	narocilo.datum_N_O = datetime.now
	narocilo.save()

	return JsonResponse({"status" : "true"})


@csrf_exempt
def obdelaj_K_N(request):#shrani v bazo kdaj je bilo naročilo obdelano in shrani status na obdelano --> Košarica

	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)	
	
	narocilo =Narocilo_K.objects.get(id = body)
	narocilo.obdelano_N_K = True
	narocilo.datum_K_N_obdelano= datetime.now
	narocilo.save()

	return JsonResponse({"status" : "true"})

@csrf_exempt
def zakljuci_O(request):#uporabnik zaključi oglas, da ni več viden v searchu
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)

	oglas= Oglas.objects.get(id = body)
	oglas.aktiven_O = False
	oglas.save()

	return JsonResponse({"status" : "true"})

@csrf_exempt
def kosarica_M(request):#spisek košaric kjer je user prodajalec
	user = request.user.id	
	kosarica = Kosarica.objects.filter(prodajalec_K= user)
	data = [{"ime_K": ogl.ime_K, "cena_K": ogl.cena_K, "kolicina_K": ogl.kolicina_K, "opis_K": ogl.opis_K , "id" : ogl.id ,"stevilo_K" : ogl.stevilo_K} for ogl in kosarica]
	return JsonResponse({ "kosarice" : data })


@csrf_exempt
def narocilo_Obdelano(request):#spisek obdelanih naročil za oglas
	user = request.user.id
	narocila = Narocilo_O.objects.filter(oglas_O_id__prodajalec_O_id = user).exclude(obdelano_N_O = 1)
	data = [{"cena_N_O": nar.cena_N_O, "kolicina_N_O": nar.kolicina_N_O, "obdelano_N_O": nar.obdelano_N_O , "datum_N_O": nar.datum_N_O , "narocilo_id" : nar.id , "kupec_O_id" : User.objects.values("ime").get(id = nar.kupec_O_id)["ime"], "oglas_O_id" : nar.oglas_O_id , "oglas_ime" : Oglas.objects.values("ime_O").get(id = nar.oglas_O_id)["ime_O"]  } for nar in narocila]
	return JsonResponse({"narocila" : data})


@csrf_exempt
def narocila_K_Moja(request):#spisek naročil kjer je user prodajalec za košarico in so neobdelana
	uporabnik = request.user.id
	
	narocilo=Narocilo_K.objects.filter(kosarica_K_id__prodajalec_K_id = uporabnik).order_by('datum_K_N').filer(obdelano_N_K = 0)
	print(narocilo)
	data = [{"cena_K_N": nar.cena_K_N, "stevilo_K_N": nar.stevilo_K_N, "datum_K_N": nar.datum_K_N , "pogostost_dostave_K": nar.pogostost_dostave_K , "id" : nar.id , "kosarica_ime" : Kosarica.objects.values("ime_K").get(id = nar.kosarica_K_id)["ime_K"]  } for nar in narocilo]
	print(data)
	return JsonResponse({"narocila" : data})
	
@csrf_exempt
def narocila_K_obdelana(request):#spisek naročil kjer je user prodajalec in so obdelana --> košarica
	narocilo=Narocilo_K.objects.filter(kosarica_K_id__prodajalec_K_id=request.user.id).order_by('datum_K_N').filter(obdelano_N_K = 1)
	
	data = [{"cena_K_N": nar.cena_K_N, "stevilo_K_N": nar.stevilo_K_N, "obdelano_N_K": nar.obdelano_N_K , "datum_K_N": nar.datum_K_N , "narocilo_id" : nar.id , "kupec_K_id" : User.objects.values("ime").get(id = nar.kupec_K_id)["ime"], "kosarica_K_id" : nar.kosarica_K_id , "Kosarica_ime" : Kosarica.objects.values("ime_K").get(id = nar.kosarica_K_id)["ime_K"] , "opis_K_N" : Kosarica.objects.values("opis_K").get(id = nar.kosarica_K_id)["opis_K"]  } for nar in narocilo]
	
	return JsonResponse({"narocila" : data})






