from django.shortcuts import render, HttpResponse
from carro.carro import Carro

def home(request):
   carro = Carro(request)
   return render(request, "ProyectoWebApp/home.html")