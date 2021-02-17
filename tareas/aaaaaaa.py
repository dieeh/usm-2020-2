from math import log
n = int(input("Ingrese un número entero mayor que uno: "))
largo_numero = int(log(n, 10) + 1)
largo_numero2 = int(len(str(n)))
print(largo_numero, largo_numero2)
