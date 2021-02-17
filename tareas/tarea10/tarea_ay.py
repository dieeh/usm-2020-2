def tiempo_min(hora, minutos):
    hora = int(hora)
    minutos = int(minutos)
    minutos_totales = ((hora * 60) + minutos)
    return minutos_totales


arch = open("registros.txt")
lista = []
d_help = {}
d = {}
for linea in arch:
    nombre, tipo, patente, h_ingreso, h_salida = linea.strip().split(";")
    hora1, minutos1 = h_ingreso.split(":")
    hora2, minutos2 = h_salida.split(":")
    t_de_ingreso = tiempo_min(hora1, minutos1)
    t_de_salida = tiempo_min(hora2, minutos2)
    t_total = t_de_salida - t_de_ingreso
    if tipo not in d:
        d[tipo] = []
    d[tipo].append((t_total, nombre, patente))
arch.close()
track = []
forma = "\t{}: {} ({})"
for key in d:
    conjunto = d[key]
    conjunto.sort()
    conjunto.reverse()
    b = conjunto[0]
    track.append((b, key))
    # if key not in d_help:
    # d_help[key]=[]
    # d_help[key].append(b)
    # print(b)
    archivo = open(key + ".txt", "w")
    i = 1
    formato = "{} - El vehiculo de {} con patente {} estuvo estacionado {} minutos\n"
    for t_total, nombre, patente in conjunto:
        archivo.write(formato.format(i, nombre, patente, t_total))
        i += 1
    archivo.close()
print("Vehiculos con mayor tiempo de estacionamiento, por tipo :")
for elemento in track:
    print(forma.format(elemento[1], elemento[0][2], elemento[0][1]))
