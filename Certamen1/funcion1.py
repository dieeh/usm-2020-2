"""
def numero_local(nombrecito):
    largo = len(nombrecito)
    b = (largo % 3) + 1
    return b


nom = input("Nombres: ")
num_loc = numero_local(nom)
print(num_loc)
"""


def suma_productos(rut):
    suma_n = 0
    i = 2  # constante a multiplicar, comenzando por la derecha: 2, 3, 4, 5, 6, 7, 1, 2
    while rut != 0:
        n = rut % 10      # obtiene el dígito de mas a la derecha
        rut = rut // 10   # elimina el dígito de mas a la derecha
        suma_n += n * i
        # A continuación, se actualiza la constante para la siguiente iteración
        i += 1
        if i == 8:    # después del 7, vuelve a 2
            i = 2
    return suma_n


def digito_verificador(x):
    b = int(x)
    p = suma_productos(b)
    verificador = 11 - (p % 11)
    if verificador == 11:
        digito = "0"
    elif verificador == 10:
        digito = "k"
    else:
        digito = verificador
    return digito


def verificador_rut(rut_completo):
    i = 0
    j = 0
    a = ""
    while i < len(rut_completo):
        if rut_completo[i] == "-":
            a = int(digito_verificador(rut_completo[j:i]))
        i += 1
    if str(a) == str(rut_completo[-1]):
        return True
    else:
        return False


z = verificador_rut("1-0")
print(z)
