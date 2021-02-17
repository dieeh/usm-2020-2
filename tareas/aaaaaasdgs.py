text = 'azul+amarillo=verde;azul+violeta=ultramar;rojo+azul=violeta;'


def agregar(resultado, color):
    # agrega guión para que el siguiente if considere el caso en que está al final
    nuevo_resultado = resultado + "-"
    if '-' + color + '-' in nuevo_resultado:
        # color ya está en resultado, se retorna sin cambios
        return resultado
    # como el color no estaba, se retorna el nuevo resultado con el color agregado al final
    return nuevo_resultado + color


def separar_colores(colores):
    i = 0
    j = 0
    lista = ""
    while i <= len(colores) - 1:
        if colores[i] == "+":
            lista = agregar(lista, colores[j:i])
            j = i + 1
        elif colores[i] == "=":
            lista = agregar(lista, colores[j:i])
        elif colores[i] == ";":
            j = i + 1
        i += 1
    return lista


abc = separar_colores(text)
print(abc)
