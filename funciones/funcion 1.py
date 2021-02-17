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


numero = int(input("Ingrese un número entero mayor que uno: "))
while numero <= 1:
    numero = int(input("Ingrese un número entero mayor que uno: "))
print(suma_divisores_propios(numero))
if primo(numero):
    print(numero, "es primo")

otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
while otro_numero <= 1:
    otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
