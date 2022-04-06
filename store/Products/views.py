from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria, Producent


def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)


def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    dane = {'produkt_user': produkt_user}
    return render(request, 'produkt.html', dane)


def producent(request, id):
    producent_user = Producent.objects.get(pk=id)
    return HttpResponse(producent_user.nazwa)
