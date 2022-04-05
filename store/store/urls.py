from django.contrib import admin
from django.urls import path
from .. Products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('kategoria/<id>/', kategoria, name='kategoria'),
    path('produkt/<id>/', produkt, name='produkt'),
    path('producent/<id>/', producent, name='producent'),

]

