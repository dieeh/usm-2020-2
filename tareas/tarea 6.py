# from leo import *


def buscar_combinacion(combinaciones, color):
    combinaciones = combinaciones + ';'
    i = 0  # índice con que se recorre el string combinaciones
    j = 0  # se mantiene como el inicio de la definición de color actual
    while i < len(combinaciones):
        if combinaciones[i] == '=':
            k = i + 1  # registra la posición donde comienza el nombre del color actual (al lado del igual)
            while combinaciones[i] != ';':
                # avanza hasta el final del nombre del color actual (al encontrar ;)
                i += 1
            if combinaciones[k:i] == color:
                # hay coincidencia entre el color actual y el buscado
                return combinaciones[j:i]
            else:
                # no hay coincidencia, se procede con la siguiente definicion de color
                j = i + 1
        i += 1
    return ''  # llegamos al final sin encontrar el color, se retorna ''


entrada = "=>"
colores = ""
color_actual = ""
combinaciones = "amarillo+rojo=naranja;azul+amarillo=verde;rojo+azul=violeta;azul+violeta=ultramar"
colores_necesitados = ""
resultados = ""
print("Ingrese los colores que quieres usar(cuando termine de escribir los colores, escriba \"termine\"): ")
while entrada != "termine":
    entrada = input()
    colores = colores + entrada + ";"
colores = colores[:-8]
print("Los colores que escribio son:")
print(colores)

for i in colores:
    if i == ";":
        colores_necesitados = colores_necesitados + buscar_combinacion(combinaciones, color_actual) + ";"
        color_actual = ""
    else:
        color_actual = color_actual + i

for i in colores_necesitados:
    if i == "+" or i == "=":
        if color_actual not in resultados:
            resultados = resultados + color_actual + "-"
        color_actual = ""
    elif i == ";":
        color_actual = ""
    else:
        color_actual = color_actual + i
resultados = resultados[:-1]
print("Los colores que necesitaras son:")
print(resultados)
