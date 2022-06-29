from django.shortcuts import render
import requests

def cotizacion(request): 
    oficial = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolaroficial')
    blue = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarblue')
    liqui = requests.get('https://api-dolar-argentina.herokuapp.com/api/contadoliqui')
    turista = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarturista')
    bolsa = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarbolsa')
    r1 = oficial.json()
    r2 = blue.json()
    r3 = liqui.json()
    r4 = turista.json()
    r5 = bolsa.json()
    resultados = {
        "oficial":r1,
        "blue":r2,
        "liqui":r3,
        "turista":r4,
        "bolsa":r5
    }
    context = {'cotizacion':resultados}
    return render(request, "dolar/dolar.html",context)