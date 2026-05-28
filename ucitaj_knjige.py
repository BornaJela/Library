import os,json,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WebApk_Projekt.settings')
django.setup()
from knjiznica.models import Autor,Knjiga,Zanr
def ucitaj_knjige():
    f=open('knjige.json','r',encoding='utf-8')
    sadrzaj=f.read()
    f.close()
    knjige=json.loads(sadrzaj)
    for podaci in knjige:
        autor,_=Autor.objects.get_or_create(
            ime=podaci['autor_ime'],
            prezime=podaci['autor_prezime']
        )
        zanr,_=Zanr.objects.get_or_create(
            zanr=podaci['zanr_naziv']
        )
        knjiga,created=Knjiga.objects.get_or_create(
            naslov=podaci['naslov'],
            defaults={
                'autor':autor,
                'zanr':zanr,
                'godina':podaci['godina'],
                'opis':podaci['opis'],
                'kolicina':podaci['kolicina']
            }
        )
if __name__=='__main__':
    ucitaj_knjige()