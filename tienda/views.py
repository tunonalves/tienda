from django.shortcuts import render
from .models import Producto
#from carro.carro import Carro


# Create your views here.

def tienda(request):    
    
    #carro=Carro(request)
    productos=Producto.objects.all()

    return render(request, "tienda/tienda.html", {"productos":productos})