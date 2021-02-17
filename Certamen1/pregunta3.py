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
            a = digito_verificador(rut_completo[j:i])
        i += 1
    if str(a) == rut_completo[-1]:
        return True
    else:
        return False


def local(n):
    Peumo = "ABCDEFG"
    Quillay = "HIJKLMNÑO"
    Canelo = "PQRSTUVWXYZ"
    if n[0] in Peumo:
        return "Peumo"
    elif n[0] in Quillay:
        return "Quillay"
    elif n[0] in Canelo:
        return "Canelo"


def numero_local(nombrecito):
    largo = len(nombrecito)
    b = (largo % 3) + 1
    return b


flag = True
while flag is True:
    print("Datos del votante:")
    rutcito = input("RUT (con guión y dígito verificador): ")
    if verificador_rut(rutcito) is True:
        ap = input("Apellidos: ")
        nom = input("Nombres: ")
        loc_vot = local(ap)
        num_loc = numero_local(nom)
        print("Le toca votar en la mesa", loc_vot, "-", num_loc)
        print("")
    else:
        flag = False
