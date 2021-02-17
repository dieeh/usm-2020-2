def suma_divisores_propios(n):
    suma = 1
    divisor = 2
    limite = n // 2
    while divisor <= limite:
        if n % divisor == 0:
            suma += divisor
        divisor += 1
    return suma


def numero_perfecto(n):
    if n == suma_divisores_propios(n):
        return True
    return False


numero = int(input("Ingrese un número entero mayor que uno: "))
while numero <= 1:
    numero = int(input("Ingrese un número entero mayor que uno: "))
if numero_perfecto(numero):
    print(numero, "es perfecto")

otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
while otro_numero <= 1:
    otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
