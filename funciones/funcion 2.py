def suma_divisores_propios(n):
    suma = 1
    divisor = 2
    limite = n // 2
    while divisor <= limite:
        if n % divisor == 0:
            suma += divisor
        divisor += 1
    return suma


def primo(n):
    suma = suma_divisores_propios(n)
    return suma == 1


def primo_de_mersenne(n):
    prim = primo(n)
    d = 0
    while prim and d <= n:
        if n == (2 ** d) - 1:
            return True
        else:
            d += 1
    return False


numero = int(input("Ingrese un número entero mayor que uno: "))
while numero <= 1:
    numero = int(input("Ingrese un número entero mayor que uno: "))
if primo(numero):
    print(numero, "es primo")
if primo_de_mersenne(numero):
    print(numero, "es primo de mersenne")

otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
while otro_numero <= 1:
    otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
