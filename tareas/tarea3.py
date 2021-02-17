from sys import exit
Humedad = int(input("Humedad de suelo: "))
Lluvia = int(input("Probabilidad de lluvia: "))
Suelo = input("Tipo de suelo: ")
Hectareas = int(input("Cantidad de hectareas: "))
ErrorHum = False
ErrorLluv = False

if Hectareas > 0:
    exit("Necesitas hectáreas para regar")

if Humedad < 0 or Humedad > 1024:
    ErrorHum = True
if Lluvia < 0 or Lluvia > 100:
    ErrorLluv = True
else:
    pass

if ErrorHum is True and ErrorLluv is True:
    exit("Error: Humedad y lluvia fuera del rango válido")
elif ErrorHum is False and ErrorLluv is True:
    exit("Error: Lluvia fuera del rango válido")
elif ErrorHum is True and ErrorLluv is False:
    exit("Error: Humedad fuera del rango válido")

if Humedad >= 700 or Lluvia >= 70:
    Riego = False
else:
    Riego = True

if not Riego:
    exit("No es necesario regar hoy.")

if Riego:
    if Suelo == "Arcilloso":
        Caudal = 1
        Tiempo = 2
        Ciclos = 2
    elif Suelo == "Limoso":
        Caudal = 3
        Tiempo = 5
        Ciclos = 2
    elif Suelo == "Arenoso":
        Caudal = 2
        Tiempo = 2
        Ciclos = 5
    else:
        exit("Error: Tipo de suelo inválido.")
else:
    pass

Litros = ((Caudal * Tiempo) * Ciclos) * Hectareas

if Riego:
    print("Se debe regar cada hectarea", Ciclos, "veces, por", Tiempo, "minutos cada vez, usando un caudal de", Caudal,
          "litros por minuto")
    print("La cantidad total de agua a utilizar será de", Litros, "litros")
