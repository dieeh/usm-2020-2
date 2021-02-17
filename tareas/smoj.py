'''
from math import sqrt
a = float(input())
b = float(input())
c = float(input())
lado1 = a + b
lado2 = a + c
lado3 = b + c
isosceles = False
escaleno = False

if lado1 > c and lado2 > b and lado3 > a:
    triangulo = True
else:
    triangulo = False

if not triangulo:
    print("No es triangulo")

if sqrt(a**2 + b**2) == c or sqrt(a**2 + c**2) == b or sqrt(b**2 + c**2) == a:
    rectangulo = True
else:
    rectangulo = False

if triangulo:
    if a == b == c:
        print("Triangulo equilatero")
    elif a == b or a == c or c == b:
        isosceles = True
    elif a != b and a != c and b != c:
        escaleno = True
else:
    pass

if rectangulo == True and isosceles == True:
    print("Triangulo isosceles rectangulo")
elif rectangulo == True and escaleno == True:
    print("Triangulo escaleno rectangulo")
else:
    pass

if rectangulo == False and isosceles == True:
    print("Triangulo isosceles")
elif rectangulo == False and escaleno == True:
    print("Triangulo escaleno")
else:
    pass
'''

'''
from math import pi
Ancho = float(input())
Largo = float(input())
Material = input()

AreaHab = Ancho * Largo
Radio1 = Ancho/2

if Material == "Algodon":
    Radio2 = Radio1 * (1/5)
elif Material == "Bambu":
    Radio2 = Radio1 * (1/4)
elif Material == "Nylon":
    Radio2 = Radio1 * (1/3)

AreaTot = pi*(Radio1**2) - pi*(Radio2**2)
Pctj = 100 - ((AreaTot/AreaHab)*100)

print(round(AreaTot, 2))
print(round(Pctj, 2),"%")
'''

'''
Numero = int(input())
if (Numero//100)**3 + ((Numero%100)//10)**3 + ((Numero%100)%10)**3 == Numero:
    Amstrong = True
else:
    Amstrong = False

if Amstrong:
    print("SI")
elif not Amstrong:
    print("NO")
'''
