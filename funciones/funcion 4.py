from math import log


def numero_narcisista(n):
    largo_numero = int(log(n, 10) + 1)
    largo_local = largo_numero
    numero_local = n
    suma = 0
    while largo_local > 0:
        digito = numero_local // 10 ** (largo_local - 1)
        numero_local -= digito * 10 ** (largo_local - 1)
        suma += digito ** largo_numero
        largo_local -= 1
    if suma == n:
        return True
    return False


numero = int(input("Ingrese un número entero mayor que uno: "))
while numero <= 1:
    numero = int(input("Ingrese un número entero mayor que uno: "))

if numero_narcisista(numero):
    print(numero, "es narcisista")

otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
while otro_numero <= 1:
    otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
