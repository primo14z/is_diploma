from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin,User)
from django.utils import timezone
from datetime import datetime


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User more imet email!")
 
        email = email.lower() 
        user = self.model(email=CustomUserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        user.is_staff=False
        user.is_admin=False
        user.is_active=True
        return user
 
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 
 
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True, )
 
    USERNAME_FIELD  = 'email'  
    ime= models.CharField(max_length=100)
    priimek= models.CharField(max_length=100)
    naslov = models.CharField(max_length=50)
    postna_st = models.IntegerField()
    kraj = models.CharField(max_length=50)
    telefonska=models.CharField(max_length = 20, default='')
    objects = CustomUserManager()
 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
 
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)


class Oglas(models.Model):
    ime_O = models.CharField(max_length = 50)
    cena_O=models.IntegerField()
    kolicina_O=models.IntegerField()
    opis_O=models.CharField(max_length= 200)
    datum_O=models.DateTimeField(default=datetime.now, blank=True)
    prodajalec_O = models.ForeignKey(User , id)
    aktiven_O = models.BooleanField(default = True)
    slika = models.FileField(upload_to ='img/Oglas/', default='img/Oglas/default.jpg')
    mesto_pridelave = models.CharField(max_length= 50, default='')

class Narocilo_O(models.Model):
    cena_N_O = models.IntegerField()
    kolicina_N_O = models.IntegerField()
    obdelano_N_O = models.BooleanField(default=False)
    datum_N_O = models.DateTimeField(default=datetime.now, blank=True)
    datum_N_O_obdelano = models.DateTimeField(default = None , blank=True)
    oglas_O =models.ForeignKey(Oglas , id)
    kupec_O = models.ForeignKey(User , id)

class Kosarica(models.Model):
    ime_K = models.CharField(max_length = 50)
    cena_K = models.IntegerField()
    kolicina_K = models.IntegerField()
    stevilo_K = models.IntegerField()
    opis_K = models.CharField(max_length = 200)
    prodajalec_K = models.ForeignKey(User, id)
    datum_K=models.DateTimeField(default=datetime.now, blank=True)
    aktiven_K = models.BooleanField(default = True)
    slika = models.FileField(upload_to ='img/Kosarica/', default='img/Kosarica/default.jpg')
    mesto_pridelave = models.CharField(max_length= 50, default='')

class Narocilo_K(models.Model):
    cena_K_N = models.IntegerField()
    stevilo_K_N = models.IntegerField()
    datum_K_N = models.DateTimeField(default=datetime.now, blank=True)
    datum_K_N_obdelano = models.DateTimeField(default = None , blank=True)
    pogostost_dostave_K = models.CharField(max_length = 40)
    kosarica_K =models.ForeignKey(Kosarica, id)
    kupec_K = models.ForeignKey(User , id)
    obdelano_N_K = models.BooleanField(default = False)

class Novica(models.Model):
    naslov_Novica = models.CharField(max_length = 100)
    opis_Novica = models.CharField(max_length = 50000)
    datum_objave = models.DateTimeField(default= None, blank= True)

class Priloga(models.Model):
    slika = models.BinaryField()
    novica_id = models.ForeignKey(Novica , id)