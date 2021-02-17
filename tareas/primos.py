"""
def suma_divisores_propios(n):
    suma = 1
    divisor = 2
    limite = n // 2
    while divisor <= limite:
        if n % divisor == 0:
            suma += divisor
        divisor += 1
    return suma


# Retorna True si el parámetro n es primo y False si no lo es.
# Esta función YA SE ENCUENTRA IMPLEMENTADA. Estudie cómo hace su trabajo.
def primo(n):
    suma = suma_divisores_propios(n)
    return suma == 1


# Retorna True si el parámetro n es primo de Mersenne y False si no lo es.
# Usted DEBE IMPLEMENTAR ESTA FUNCIÓN.
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
if primo_de_mersenne(numero):
    print(numero, "es primo de mersenne")
else:
    print("no es primo de mersenne")
"""


def numero_narcisista(n):
    largo = int(len(str(n)))
    numbr = n
    largototal = largo
    suma = 0
    while largo >= 0:
        factor = (numbr // 10 ** (largo - 1)) ** largototal
        numbr = n - (numbr // 10 ** (largo - 1)) * 10 ** largo
        suma += round(factor, 1)
        largo -= 1
        print(suma)
    if suma == n:
        return True
    else:
        return False


numero = int(input("Ingrese un número entero mayor que uno: "))

if numero_narcisista(numero):
    print(numero, "es narcisista")
