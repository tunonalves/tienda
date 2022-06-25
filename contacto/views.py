from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage(
                "Mensaje desde App Django",
                "El usuario: {} email: {} contenido: \n\n {}".format(nombre,email,contenido),
                "",["tunonalves@gmail.com"],reply_to=[email]
            )

            inform = formulario_contacto.cleaned_data
            send_mail(inform['nombre'],inform['contenido'],inform.get('email','fedeta86@gmail.com'),['tunonalves@gmail.com'],)
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?error")
    return render(request,"contacto/contacto.html",{'miformulario':formulario_contacto})


#de otro ejercicio no se usa 

'''def contactonuevo(request):
    if request.method=="POST":
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            inform = miFormulario.cleaned_data
            send_mail(inform['asunto'],inform['mensaje'],inform.get('email','fedeta86@gmail.com'),['tunonalves@gmail.com'],)
            return render(request,"appgestionpedidos/gracias.html")
    else:
        miFormulario = FormularioContacto()
    return render(request,"appgestionpedidos/contactonuevo.html",{"form":miFormulario})'''

'''
def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["fedeta86@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})'''
