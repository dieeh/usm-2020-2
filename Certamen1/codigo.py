def suma_productos(rut):
    suma_n = 0
    i = 2
    while rut != 0:
        n = rut % 10
        rut = rut // 10
        suma_n += n * i
        i += 1
        if i == 8:
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
print(suma_productos(rut))
