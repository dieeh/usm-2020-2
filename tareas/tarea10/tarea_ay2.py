archivo = open("registros.txt", "r")
lista = []
lista2 = []
for linea in archivo:
    nombre, tipo, patente, hora_i, hora_s = linea.strip().split(";")
    if tipo not in lista2:
        lista2.append(tipo)
    hora_i = hora_i.split(":")
    hora_f = hora_s.split(":")
    minutos = ((int(hora_f[0]) - int(hora_i[0])) * 60) + \
        (int(hora_f[1]) - int(hora_i[1]))
    if tipo not in lista2:
        lista2.append(tipo)
    lista.append((tipo, nombre, patente, minutos))
