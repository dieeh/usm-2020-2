# Nombre: Diego Eduardo Paz Letelier
# Paralelo: 211

def obtener_representante(nombre_archivo):
    formato = "{}.txt"
    archivo = open(formato.format(nombre_archivo))
    lista = {}
    for linea in archivo:
        voto1, voto2, voto3 = linea.strip().split(";")
        voto1a = voto1.lower()
        voto2a = voto2.lower()
        voto3a = voto3.lower()
        if voto1a == voto2a == voto3a:
            lista[voto1a] += 1
        else:
            if voto1a not in lista:
                lista[voto1a] = 1
            elif voto1a in lista:
                lista[voto1a] += 1
            if voto2a not in lista:
                lista[voto2a] = 1
            elif voto2a in lista:
                if voto2a == voto1a or voto2a == voto3a:
                    lista[voto2a] += 0
                else:
                    lista[voto2a] += 1
            if voto3a not in lista:
                lista[voto3a] = 1
            elif voto3a in lista:
                if voto3a == voto2a or voto3a == voto1a:
                    lista[voto3a] += 0
                else:
                    lista[voto3a] += 1
    abc = []
    for elemento in lista:
        abc.append((lista[elemento], elemento))
    abc.sort()
    abc.reverse()
    return abc[0][1].upper(), abc[0][0]


a = obtener_representante("votos")
print(a)
