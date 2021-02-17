'''
Dividendo = int(input())
Divisor  = int(input())

if not Dividendo%Divisor == 0:
    print("La división no es exacta")
else:
    print("La división es exacta")

print("Cociente:",(Dividendo//Divisor))
print("Resto:",(Dividendo%Divisor))
'''

'''
a = float(input("Ingrese a:"))
b = float(input("Ingrese b:"))
c = float(input("Ingrese c:"))
lado1 = a + b
lado2 = a + c
lado3 = b + c

if lado1 > c and lado2 > b and lado3 > a:
    if a == b == c:
        print("El triángulo es equilátero")
    elif a == b or b == c or c == a:
        print("El triángulo es isósceles")
    elif a != b != c:
        print("El triángulo es escaleno")
else:
    print("El triángulo no es válido")
'''


'''
n1 = int(input())
n2 = int(input())

print(min(n1,n2),max(n1,n2))
'''

n1 = int(input())
n2 = int(input())
n3 = int(input())

if max(n1, n2, n3) > n1 > min(n1, n2, n3):
    print(min(n1, n2, n3), n1, max(n1, n2, n3))
elif max(n1, n2, n3) > n2 > min(n1, n2, n3):
    print(min(n1, n2, n3), n2, max(n1, n2, n3))
else:
    print(min(n1, n2, n3), n3, max(n1, n2, n3))
