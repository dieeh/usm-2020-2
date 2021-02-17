"""
Busca el color indicado dentro de combinaciones y retorna un string con
los colores que lo componen, en el formato: color1+color2=color3.
En caso de no encontrar el color, retorna un string vacío.
combinaciones="amarillo+rojo=naranja;azul+amarillo=verde;..."
"""


def buscar_combinacion(combinaciones, color):
    combinaciones = combinaciones + ';'
    i = 0  # índice con que se recorre el string combinaciones
    j = 0  # se mantiene como el inicio de la definición de color actual
    while i < len(combinaciones):
        if combinaciones[i] == '=':
            # registra la posición donde comienza el nombre del color actual (al lado del igual)
            k = i + 1
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


'''
Agrega color al string resultado, siempre y cuando no exista previamente,
retornando el nuevo resultado.
Ejemplo de resultado: '−rojo−verde−amarillo'
'''


def agregar(resultado, color):
    # agrega guión para que el siguiente if considere el caso en que está al final
    nuevo_resultado = resultado + "-"
    if '-' + color + '-' in nuevo_resultado:
        # color ya está en resultado, se retorna sin cambios
        return resultado
    # como el color no estaba, se retorna el nuevo resultado con el color agregado al final
    return nuevo_resultado + color


combinaciones = input("Ingrese su lista de combinación de colores, por ejemplo color1+color2=colorresultante1;color3+color4=colorresultante2;etc: ")
colores = input("Ingrese los colores que quiere, por ejemplo colorresultante1;colorresultante2;etc: ") + ";"
color_necesitado = ""
combinacion_necesitada = ""
contador1 = 0
while contador1 < len(colores):
    while colores[contador1] != ";":
        color_necesitado += colores[contador1]
        contador1 += 1
    if color_necesitado in buscar_combinacion(combinaciones, color_necesitado):
        combinacion_necesitada += buscar_combinacion(
            combinaciones, color_necesitado)
        combinacion_necesitada += ";"
        color_necesitado = ""
    contador1 += 1
juntar_color = ""
juntar_color_suma = ""
contador2 = 0
while contador2 < len(combinacion_necesitada):
    if combinacion_necesitada[contador2] == "+":
        juntar_color_suma += juntar_color
        juntar_color_suma += "-"
        contador2 += 1
        juntar_color = ""
    elif combinacion_necesitada[contador2] != "=" and combinacion_necesitada[contador2] != "+" and combinacion_necesitada != ";":
        juntar_color += combinacion_necesitada[contador2]
        contador2 += 1
    elif combinacion_necesitada[contador2] == "=":
        juntar_color_suma += juntar_color
        juntar_color_suma += "-"
        juntar_color = ""
        while combinacion_necesitada[contador2] != ";":
            contador2 += 1
        contador2 += 1
contador3 = 0
colores_finales = ""
while contador3 < len(juntar_color_suma):
    if juntar_color_suma[contador3] != "-":
        juntar_color += juntar_color_suma[contador3]
        contador3 += 1
    else:
        colores_finales = agregar(colores_finales, juntar_color)
        juntar_color = ""
        contador3 += 1
if colores_finales == "":
    contador4 = ""
    for letra in colores:
        if letra == ";":
            letra = "-"
        contador4 += letra
    print("Los colores que debes comprar son:", contador4[:-1])
else:
    print("Los colores que debes comprar son:", colores_finales[1:])
