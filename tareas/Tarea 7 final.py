from t7_base import*


def obtener_info_pedido(pedidos, id):
    n = 0
    while n != len(pedidos):
        if (pedidos[n])[0] == id:
            return pedidos[n][1:]
        n = n + 1
    return []


def pedidos_por_fecha(pedidos, dd, mm, aaaa):
    n = 0
    productos_fecha = []
    while n != len(pedidos):
        if pedidos[n][4][0] == aaaa and pedidos[n][4][1] == mm and pedidos[n][4][2] == dd:
            productos_fecha.append((pedidos[n])[0])
        n = n + 1
    return productos_fecha


print("Ingrese la fecha para registrar las entregas:")
año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))

estafecha = pedidos_por_fecha(pedidos, dia, mes, año)

n = 0
while n != len(estafecha):
    informacion = obtener_info_pedido(pedidos, estafecha[n])
    print("Procesando pedido", estafecha[n],
          "para:", informacion[0], informacion[1])
    k = 0
    while k != len(productos_x_pedido):
        if (productos_x_pedido[k])[0] == estafecha[n]:
            i = 0
            while i != len(productos_x_pedido[k][1]):
                print(productos_x_pedido[k][1][i])
                productos_entregados.append(
                    [estafecha[n], (productos_x_pedido[k][1][i]), informacion[0], informacion[1]])
                i = i + 1
        k = k + 1
    n = n + 1
print("Hasta la fecha se han entregado",
      len(productos_entregados), "productos")
