# Nombre: Diego Eduardo Paz Letelier
# Paralelo: 211

def escritura(archivo, tipo):
    d = []
    file = open(archivo, "r")
    formato = "{}.txt"
    out = open(formato.format(tipo), "w")
    formato2 = "{} - El vehiculo de {} con patente {} estuvo estacionado {} minutos.\n"
    i = 1
    for linea in file:
        nombre, tipo2, patente, h_ing, h_sal = linea.strip().split(";")
        hora_i = h_ing.split(":")
        hora_f = h_sal.split(":")
        minutos = ((int(hora_f[0]) - int(hora_i[0])) * 60) + \
                  (int(hora_f[1]) - int(hora_i[1]))
        if tipo2 == tipo:
            d.append((minutos, nombre, patente))
    d.sort()
    d.reverse()
    for elemento in d:
        minutos2, nombre2, patente2 = elemento
        out.write(formato2.format(i, nombre2, patente2, minutos2))
        i += 1
    file.close()
    out.close()
    return d[0][1:], tipo, i - 1


archivo = open("registros.txt", "r")
formato = "\t{}: {} ({})"
tipos = []
inf = []    # [(('Fernando Torres', 'RFDE51'), 'Automovil', 3), (('Valentina Reyes', 'ALFY87'), 'Camioneta', 2), (('Sofia Zenteno', 'LLYG34'), 'Moto', 2)]
for linea in archivo:
    _, tipo, _, _, _ = linea.strip().split(";")
    if tipo not in tipos:
        tipos.append(tipo)
for tipo1 in tipos:
    inf.append(escritura("registros.txt", tipo1))
archivo.close()
print("Vehículos con mayor tiempo de estacionamiento, por tipo:")
contador = 0
for tupla in inf:
    print(formato.format(tupla[1], tupla[0][0], tupla[0][1]))
    contador += tupla[2]
print("Total de vehículos en el día:", contador)
