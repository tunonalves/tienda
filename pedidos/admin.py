from django.contrib import admin
from pedidos.models import LineaPedido, Pedido


admin.site.register([Pedido,LineaPedido])