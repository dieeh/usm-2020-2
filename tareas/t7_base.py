# Nombre: Diego Eduardo Paz Letelier
# Paralelo: 211


pedidos = [
    [5234, "Las Casitas #123", "+56987654321", 35990, [2020, 11, 15]],
    [6532, "Alto del Python #385", "+56224523423", 140000, [2020, 11, 14]],
    [6558, "Calle Sin Salida #1314", "+56957258379", 15840, [2020, 11, 14]],
    [6722, "Tosta Dora #1818", "+56912457896", 25000, [2020, 11, 12]],
    [7342, "Pasaje cerrado #8843", "+56862493854", 3750, [2020, 11, 14]],
    [7558, "Las Teteras #7785", "+56968635215", 80000, [2020, 11, 13]]
]

productos_x_pedido = [
    [5234, ["Zapatillas Ribuk o Naik", "Pantalones finos"]],
    [6532, ["Mouse USB", "Teclado USB", "Fax/modem 14kbps", "Pantalla Gamer 7pulg."]],
    [6558, ["Autito de Juguete", "Libro de Dinosaurios"]],
    [6722, ["Shampoo", "Jabon", "Cepillo", "Esponja"]],
    [7342, ["Mascarillas", "Lapiz Pasta Negro"]],
    [7558, ["Mancuernas", "Cuerda para saltar", "Traje de baño"]]
]

productos_entregados = [
    [6722, "Shampoo", "Tosta Dora #1818", "+56912457896"],
    [6722, "Jabon", "Tosta Dora #1818", "+56912457896"],
    [6722, "Cepillo", "Tosta Dora #1818", "+56912457896"],
    [6722, "Esponja", "Tosta Dora #1818", "+56912457896"]
]


def obtener_info_pedido(pedido, id):
    i = 0
    b = []
    while i < len(pedido):
        b = list(pedido[i])
        if b[0] == id:
            return b[1:]
        i += 1
    return []


def obtener_productos(productos, id):
    i = 0
    b = []
    while i < len(productos):
        b = list(productos[i])
        if b[0] == id:
            return b[1:]
        i += 1
    return []


def pedidos_por_fecha(pedido, dd, mm, aaaa):
    fecha = [aaaa, mm, dd]
    pedidos_id = []
    i = 0
    while i < len(pedido):
        c = list(pedido[i])
        if c[-1] == fecha and (c[0] not in pedidos_id):
            pedidos_id.append(c[0])
        i += 1
    return pedidos_id


def anadir_entrega(identificador, elemento, lista_entrega, lista_pedidos):
    k = []
    z = list(obtener_info_pedido(lista_pedidos, identificador))
    if identificador not in k:
        k.insert(0, identificador)
    if elemento not in k:
        k.insert(1, elemento)
    k.insert(2, z[0])
    k.insert(3, z[1])
    lista_entrega.append(k)
    return lista_entrega


print("Ingrese la fecha para registrar las entregas: ")
ano = int(input("Año: "))
mes = int(input("Mes: "))
dia = int(input("Día: "))
pedidos_del_dia = pedidos_por_fecha(pedidos, dia, mes, ano)
j = 0
while j < len(pedidos_del_dia):
    a = list(obtener_info_pedido(pedidos, pedidos_del_dia[j]))
    print("Procesando pedido",
          pedidos_del_dia[j], "para:", a[0], "(" + a[1] + ")")
    w = list(obtener_productos(productos_x_pedido, pedidos_del_dia[j]))
    for elemento in w[0]:
        print("    ", elemento)
        y = list(anadir_entrega(
            pedidos_del_dia[j], elemento, productos_entregados, pedidos))
        productos_entregados = y
    j += 1
print("Hasta la fecha se han entregado",
      len(productos_entregados), "productos.")
