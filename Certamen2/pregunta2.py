# Nombre: Diego Eduardo Paz Letelier
# Paralelo: 211

def filtrar_locales(nombre_archivo, rango):
    formato = "{}.txt"
    formato2 = "Locales de tipo {} que están a distancia {} o menos:\n"
    formato3 = "\t{}, calificación {}, precio: {}\n"
    archivo = open(formato.format(nombre_archivo), "r")
    lista = []
    lista2 = []
    for linea in archivo:
        nombre, tipo, coord, calificacion, precio = linea.strip().split(";")
        x, y = coord.split(",")
        distancia = (int(x)**2 + int(y)**2)**0.5
        if distancia <= rango:
            lista.append((precio, nombre, tipo, calificacion))
        if tipo not in lista2:
            lista2.append(tipo)
    lista.sort()
    for tipo in lista2:
        out = open(formato.format(tipo), "w")
        out.write(formato2.format(tipo, rango))
        for elemento in lista:
            precio2, nombre2, tipo2, calificacion2 = elemento
            if tipo2 == tipo:
                out.write(formato3.format(nombre2, calificacion2, precio2))
    archivo.close()
    out.close()
    return len(lista)


a = filtrar_locales("locales", 10)
print(a)
