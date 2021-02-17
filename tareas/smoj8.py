tabla = [
    (65, 'A'), (66, 'B'), (67, 'C'), (68, 'D'), (69, 'E'),
    (70, 'F'), (71, 'G'), (72, 'H'), (73, 'I'), (74, 'J'),
    (75, 'K'), (76, 'L'), (77, 'M'), (78, 'N'), (79, 'O'),
    (80, 'P'), (81, 'Q'), (82, 'R'), (83, 'S'), (84, 'T'),
    (85, 'U'), (86, 'V'), (87, 'W'), (88, 'X'), (89, 'Y'),
    (90, 'Z')
]

mensaje = [(42, 10, 4), (479, -100, 5), (70, 1, 7), (65, 500, 1)]

'''
def decifrar(lista, tabla):
    largo = len(lista)
    inicio = 0
    mensaje = []
    javi = ""
    for (numero, multiplicador, cantidad) in lista:
        valor = numero + (multiplicador * (cantidad - 1))
        mensaje.append(valor)
    resultado = []
    for variable in mensaje:
        for varikaka in tabla:
            if variable == varikaka[0]:
                resultado.append(varikaka[1])
    while inicio <= (largo - 1):
        javi += resultado[inicio]
        inicio += 1
    return javi
'''


def decifrar(lista, tabla):
    i = 0
    msg = []
    text = ""
    while i < len(lista):
        codigo, incremento, veces = lista[i]
        code = codigo + (incremento * (veces - 1))
        j = 0
        while j < len(tabla):
            if code == tabla[j][0]:
                msg.append(tabla[j][1])
            j += 1
        i += 1
    for letra in msg:
        text += letra
    return text


z = decifrar(mensaje, tabla)
print(z)
