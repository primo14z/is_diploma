from django import forms
from KmetApp.models import *


class OglasForm(forms.ModelForm):
	"""docstring for OglasForm"""
	def __init__(self, arg):
		super(OglasForm, self).__init__()
		self.arg = arg
		
class DocumentForm(forms.ModelForm):
	class Meta:
		model = Oglas
		fields= ['ime_O' ,'cena_O', 'kolicina_O','opis_O', 'datum_O','aktiven_O', 'slika', "mesto_pridelave"]

class KosaricaForm(forms.ModelForm):
	def __init__(self, arg):
		super(KosaricaForm, self).__init__()
		self.arg= arg

class DocumentForm1(forms.ModelForm):
	class Meta:
		model = Kosarica
		fields= ['ime_K' , 'cena_K', 'kolicina_K' , 'stevilo_K' , 'opis_K' , 'prodajalec_K' , 'datum_K', 'aktiven_K' , 'slika', 'mesto_pridelave']			