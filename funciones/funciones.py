"""
Este es el único archivo que se sube a AULA para la entrega
Nombre: Diego Eduardo Paz Letelier
Paralelo: 211
"""
from math import log


# Retorna la suma de los divisores propios del parámetro n.
# NO MODIFIQUE esta función. Decida si la puede utilizar para sus funciones.
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


# Retorna True si el parámetro n es número perfecto y False si no lo es.
# Usted DEBE IMPLEMENTAR ESTA FUNCIÓN.
def numero_perfecto(n):
    if n == suma_divisores_propios(n):
        return True
    return False


# Retorna True si el parámetro n es número narcisista y False si no lo es.
# Usted DEBE IMPLEMENTAR ESTA FUNCIÓN.
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


# Retorna True si los parámetros n y m son números amigos y False si no lo son.
# Usted DEBE IMPLEMENTAR ESTA FUNCIÓN.
def son_amigos(n, m):
    if suma_divisores_propios(n) == m and suma_divisores_propios(m) == n:
        return True
    return False
