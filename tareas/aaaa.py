# Un año es bisiesto si es divisible por 4
# excepto si es divisible por 100 y no por 400

año = int(input("Año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("True")
else:
    print("False")
