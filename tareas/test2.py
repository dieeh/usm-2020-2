pedidos = [
    [5234, "Las Casitas #123", "+56987654321", 35990, [2020, 11, 15]],
    [6532, "Alto del Python #385", "+56224523423", 140000, [2020, 11, 14]],
    [6558, "Calle Sin Salida #1314", "+56957258379", 15840, [2020, 11, 14]],
    [6722, "Tosta Dora #1818", "+56912457896", 25000, [2020, 11, 12]],
    [7342, "Pasaje cerrado #8843", "+56862493854", 3750, [2020, 11, 14]],
    [7558, "Las Teteras #7785", "+56968635215", 80000, [2020, 11, 13]]
]

productos_entregados = [
    [6722, "Shampoo", "Tosta Dora #1818", "+56912457896"],
    [6722, "Jabon", "Tosta Dora #1818", "+56912457896"],
    [6722, "Cepillo", "Tosta Dora #1818", "+56912457896"],
    [6722, "Esponja", "Tosta Dora #1818", "+56912457896"]
]


def obtener_info_pedido(pedido, ide):
    i = 0
    b = []
    while i < len(pedido):
        b = list(pedido[i])
        if b[0] == ide:
            return b[1:]
        i += 1
    return []


def anadir_entrega(identificador, elemento, lista_entrega, lista_pedidos):
    w = []
    z = list(obtener_info_pedido(lista_pedidos, identificador))
    if identificador not in w:
        w.insert(0, identificador)
    if elemento not in w:
        w.insert(1, elemento)
    w.insert(2, z[0])
    w.insert(3, z[1])
    lista_entrega.append(w)
    return lista_entrega


v = anadir_entrega(6558, "Libro de Dinosaurios", productos_entregados, pedidos)
print(v)
