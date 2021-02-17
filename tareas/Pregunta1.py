def obtener_representante(nombre_archivo):
    votaciones = {}
    a = 0
    mayor = -1
    documento = open(nombre_archivo)
    for linea in documento:
        lin = linea.strip().lower().split(";")
        voto = lin
        if voto[0] == voto[1]:
            del(voto[0])
        if voto[0] == voto[1]:
            del(voto[0])
        for participantes in voto:
            if participantes not in votaciones:
                votaciones[participantes] = 0
            if participantes in votaciones:
                votaciones[participantes] = votaciones[participantes] + 1
    for alumnos in votaciones:
        if mayor <= votaciones[alumnos]:
            mayor = votaciones[alumnos]
            ganador = (alumnos.upper(), mayor)
            a = a + 1
    return((ganador))
    documento.close()


print(obtener_representante('votos.txt'))
