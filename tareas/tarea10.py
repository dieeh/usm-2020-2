def escritura(archivo, tipo):
    file = open(archivo, "r")
    formato = "{}.txt"
    out = open(formato.format(tipo), "w")
    formato2 = "{} - El vehiculo de {} con patente {} estuvo estacionado {} minutos.\n"
    i = 0
    for linea in file:
        nombre, tipo2, patente, h_ing, h_sal = linea.strip().split(";")
        hora_i = h_ing.split(":")
        hora_f = h_sal.split(":")
        minutos = (int(hora_f[0]) - int(hora_i[0]) * 60) + \
            (int(hora_f[1]) - int(hora_i[1]))
        if tipo2 == tipo:
            out.write(formato2.format(i, nombre, patente, minutos))
            i += 1
    file.close()
    out.close()
    return


archivo = open("registros.txt", "r")
formato = "{}.txt"
tipos = []
for linea in archivo:
    _, tipo, _, _, _ = linea.strip().split(";")
    if tipo not in tipos:
        tipos.append(tipo)
for tipo1 in tipos:
    escritura("registros.txt", tipo1)
