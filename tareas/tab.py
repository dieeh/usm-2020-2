from math import *
ancho = int(input(""))
largo = int(input(""))
material = str(input(""))

pieza = ancho * largo
circulo_g = (((ancho / 2) ** 2) * pi)

if material == "Algodon":
    circulo_c = (((ancho / 10) ** 2) * pi)
    alfombra = (circulo_g - circulo_c)
elif material == "Bambu":
    circulo_c = (((ancho / 8) ** 2) * pi)
    alfombra = (circulo_g - circulo_c)
elif material == "Nylon":
    circulo_c = (((ancho / 6) ** 2) * pi)
    alfombra = (circulo_g - circulo_c)
else:
    pass

ecuacion = (pieza - alfombra)
ecuacion_2 = (ecuacion / pieza)
porcentaje_p = (ecuacion_2 * 100)

print(round(alfombra, 2))
print(round(porcentaje_p, 2), "%")
