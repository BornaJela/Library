"""
URL configuration for WebApk_Projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from knjiznica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.popis_knjiga,name='popis_knjiga'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registracija/',views.registracija,name='registracija'),
    path('dodaj-knjigu/',views.dodaj_knjigu,name="dodaj_knjigu"),
    path('uredi-knjigu/<int:id>/',views.uredi_knjigu,name="uredi_knjigu"),
    path('obrisi-knjigu/<int:id>/',views.obrisi_knjigu,name="obrisi_knjigu"),
    path('posudi/<int:id>/',views.posudi_knjigu,name="posudi_knjigu"),
    path('vrati/<int:id>/',views.vrati_knjigu,name="vrati_knjigu"),
    path('moje-posudbe/',views.moje_posudbe,name="moje_posudbe"),
    path('statistika/',views.statistika,name="statistika"),
]
