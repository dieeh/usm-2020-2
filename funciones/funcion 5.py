def suma_divisores_propios(n):
    suma = 1
    divisor = 2
    limite = n // 2
    while divisor <= limite:
        if n % divisor == 0:
            suma += divisor
        divisor += 1
    return suma


def son_amigos(n, m):
    if suma_divisores_propios(n) == m and suma_divisores_propios(m) == n:
        return True
    return False


numero = int(input("Ingrese un número entero mayor que uno: "))
while numero <= 1:
    numero = int(input("Ingrese un número entero mayor que uno: "))

otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
while otro_numero <= 1:
    otro_numero = int(input("Ingrese otro número entero mayor que uno: "))

if son_amigos(numero, otro_numero):
    print(numero, "y", otro_numero, "son amigos")
