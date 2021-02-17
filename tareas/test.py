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


def obtener_info_pedido(pedido, id):
    i = 0
    b = []
    while i < len(pedido):
        b = list(pedido[i])
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


def obtener_productos(productos, id):
    i = 0
    b = []
    while i < len(productos):
        b = list(productos[i])
        if b[0] == id:
            return b[1:]
        i += 1
    return []


a = obtener_info_pedido(pedidos, 6722)
print(a)
