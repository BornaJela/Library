from django.db import models
from django.contrib.auth.models import User
class Autor(models.Model):
    ime=models.CharField(max_length=100)
    prezime=models.CharField(max_length=100)
    def __str__(this):
        return f'{this.ime} {this.prezime}'
    class Meta:
        verbose_name_plural="Autori"
class Zanr(models.Model):
    zanr=models.CharField(max_length=100)
    def __str__(this):
        return this.zanr
    class Meta:
        verbose_name_plural="Žanrovi"
class Knjiga(models.Model):
    naslov=models.CharField(max_length=100)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    zanr=models.ForeignKey(Zanr,on_delete=models.CASCADE)
    opis=models.TextField()
    godina=models.IntegerField()
    kolicina=models.IntegerField(default=0)
    puta_posudjena=models.IntegerField(default=0)
    def __str__(this):
        return this.naslov
    class Meta:
        verbose_name_plural="Knjige"
class Posudba(models.Model):
    korisnik=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posudba_korisnika')
    knjiga=models.ForeignKey(Knjiga,on_delete=models.CASCADE,related_name='posudba_knjige')
    datum_posudbe=models.DateTimeField(auto_now_add=True)
    datum_povrata=models.DateTimeField(null=True,blank=True)
    je_vraceno=models.BooleanField(default=False)
    def __str__(this):
        return f'{this.korisnik.username} - {this.knjiga.naslov}'