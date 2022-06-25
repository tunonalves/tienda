from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pedidos.models import LineaPedido, Pedido
from carro.carro import Carro
from django.contrib import messages


def pedidos(request):
    return render(request,"pedidos/pedidos.html")

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedidos = list()
    for key,value in carro.carro.items():
        lineas_pedidos.append(LineaPedido(
            producto_id = key,
            cantidad = value ["cantidad"],
            user = request.user,
            pedido = pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedidos)
    enviar_mail(
                pedido=pedido,
                lineas_pedidos=lineas_pedidos,
                nombreuser=request.username,
                emailuser=request.usermail
    )
    messages.success(request,"El pedido se creo correctamente")
    return redirect("../tienda")