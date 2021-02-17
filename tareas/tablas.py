a = float(input())
b = float(input())
c = float(input())

if (a + b > c) and (a + c > b) and (b + c > a):
  if a == b == c:
    print("Triangulo equilatero")
  elif a != b and b != c and a != c:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
      print("Triangulo escaleno rectángulo")
    else:
      print("Triangulo escaleno")
  elif a == b or a == c or b == c:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
      print("Triangulo isosceles rectángulo")
    else:
      print("Triangulo isosceles")
else:
  print("No es un triangulo")
