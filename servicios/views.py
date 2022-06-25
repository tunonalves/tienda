from django.shortcuts import render
from servicios.models import Servicio
from .forms import formServ

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})

def formserv(request):
    data = {
        'formServ' : formServ()
    }
    if request.method == 'POST':
        forms = formServ(data=request.POST)
        if forms.is_valid():
            forms.save()
        else:
            data['formServ'] = forms
    return render(request,"servicios/newserv.html",data)