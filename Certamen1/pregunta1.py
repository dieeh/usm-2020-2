# Nombre: Diego Paz Letelier
# Paralelo: 211

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


def digito_verificador(rut):
    p = suma_productos(rut)
    verificador = 11 - (p % 11)
    digito = ""
    if verificador == 11:
        digito = "0"
    elif verificador == 10:
        digito = "k"
    else:
        digito = verificador
    return digito


rut = int(input('Ingrese su RUT: '))
d = digito_verificador(rut)
rut_completo = str(rut) + '-' + str(d)
print(rut_completo)
