from math import log
n = int(input("Ingrese un número entero mayor que uno: "))
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
    narcisista = True
else:
    narcisista = False

if narcisista:
    print(n, "es narcisista")
else:
    print(n, "no es narcisista")

'''
operacion = 3540 // 10**3
operacion2 = 3540 - (3540 // 10**3)*10**3

print(operacion)
print(operacion2)
'''
