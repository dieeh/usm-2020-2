n_hectareas = int(input("Número de hectáreas: "))
humedad_suelo = int(input("Humedad del suelo (0-1024): "))
probabilidad_lluvia = int(input("Probabilidad de lluvia(0-100): "))
tipo_suelo = input("Tipo de Suelo (Arcilloso/Limoso/Arenoso):")

'''Nunca se riega cuando la humedad del suelo es mayor o igual a 700, ni tampoco cuando la
probabilidad de lluvia es mayor o igual 70'''

if n_hectareas <= 0:
    print("No existen hectáreas en las cuales trabajar, se requiere de un valor mayor a 0")
elif humedad_suelo < 0:
    print("Valor de humedad del suelo fuera de rango")
elif probabilidad_lluvia < 0:
    print("Valor de probabilidad de lluvia fuera de rango")
elif not (tipo_suelo == "Arcilloso" or tipo_suelo == "Limoso" or tipo_suelo == "Arenoso"):
    print("Ingrese un tipo de suelo valido (Arcilloso/Limoso/Arenoso)")
elif humedad_suelo >= 700 and probabilidad_lluvia >= 70:
    print("No es necesario regar en el día")
else:
    if tipo_suelo == 'Arcilloso':
        caudal = 1
        tiempo = 2
        n_ciclos = 2
        litros = n_hectareas*4
    elif tipo_suelo == 'Limoso':    
        caudal = 3
        tiempo = 5
        n_ciclos = 2
        litros = n_hectareas*30
    else:
        caudal = 2
        tiempo = 2
        n_ciclos = 5
        litros = n_hectareas*20
    print('Se debe regar', n_ciclos, "veces ese día, por", tiempo, 'minutos cada vez, usando un caudal de', caudal, 'litros por minutos. La cantidad total de agua a utilizar sería de', litros, 'litros')
