from random import randint
Jugador1 = input("Competidor 1: ")
Jugador2 = input("Competidor 2: ")
ronda = 1
rondas_ganadas1 = 0
rondas_ganadas2 = 0
intentos1 = 1
intentos2 = 1
totalintentos1 = 0
totalintentos2 = 0
flag = True

while (rondas_ganadas1 < rondas_ganadas2 + 3) and (rondas_ganadas2 < rondas_ganadas1 + 3):
    print("Ronda", ronda, ":")
    numero = randint(1111, 9999)
    flag = True
    intentos1 = 1
    intentos2 = 1
    while flag:
        input1 = int(input("Ingrese un número, " + str(Jugador1) + ": "))
        aciertos = 0
        digit1a = input1 // 1000
        digit2a = input1 % 1000 // 100
        digit3a = input1 % 100 // 10
        digit4a = input1 % 10 // 1
        if digit1a == numero // 1000:
            aciertos += 1
        if digit2a == numero % 1000 // 100:
            aciertos += 1
        if digit3a == numero % 100 // 10:
            aciertos += 1
        if digit4a == numero % 10 // 1:
            aciertos += 1
        if aciertos == 4:
            rondas_ganadas1 += 1
            print("Ha logrado acertar a", aciertos, "valores")
            print("La ronda", ronda, "la ganó",
                  Jugador1, "en", intentos1, "intentos")
            print("Jugador", Jugador1, "lleva", rondas_ganadas1,
                  ",", "Jugador", Jugador2, "lleva", rondas_ganadas2)
            totalintentos1 += intentos1
            flag = False
            break
        else:
            print("Ha logrado acertar a", aciertos, "valores")
            intentos1 += 1
        input2 = int(input("Ingrese un número, " + str(Jugador2) + ": "))
        aciertos = 0
        digit1b = input2 // 1000
        digit2b = input2 % 1000 // 100
        digit3b = input2 % 100 // 10
        digit4b = input2 % 10 // 1
        if digit1b == numero // 1000:
            aciertos += 1
        if digit2b == numero % 1000 // 100:
            aciertos += 1
        if digit3b == numero % 100 // 10:
            aciertos += 1
        if digit4b == numero % 10 // 1:
            aciertos += 1
        if aciertos == 4:
            rondas_ganadas2 += 1
            print("Ha logrado acertar a", aciertos, "valores")
            print("La ronda", ronda, "la ganó",
                  Jugador2, "en", intentos2, "intentos")
            print("Jugador", Jugador1, "lleva", rondas_ganadas1,
                  ",", "Jugador", Jugador2, "lleva", rondas_ganadas2)
            totalintentos2 += intentos2
            flag = False
            break
        else:
            print("Ha logrado acertar a", aciertos, "valores")
            intentos2 += 1
    ronda += 1

promedio1 = totalintentos1 / (ronda - 1)
promedio2 = totalintentos2 / (ronda - 1)

if rondas_ganadas2 + 3 == rondas_ganadas1:
    print("Juego Terminado. ¡Felicitaciones!")
    print("El Gran Ganador es ", Jugador1,
          ", con", promedio1, "intentos promedio")
else:
    print("Juego Terminado. ¡Felicitaciones!")
    print("El Gran Ganador es", Jugador2,
          ", con", promedio2, "intentos promedio")
