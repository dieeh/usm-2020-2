from estudiantes import*


def digito_verificador(rut):
    p = suma_productos(rut)
    verificador = 11 - (p % 11)
    if verificador == 11:
        return "0"
    elif verificador == 10:
        return "k"
    else:
        return verificador
