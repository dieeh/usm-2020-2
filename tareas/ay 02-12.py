# C3 2019-2
def filtrar(nombre_archivo, año):
    archivo = open(nombre_archivo, 'r')
    dicc = {}
    for linea in archivo:
        campos = linea.strip().split(':')
        nombre = campos[1]
        pais = campos[2]
        fecha = campos[3].split('-')
        if int(fecha[2]) == año:
            if pais not in dicc:
                dicc[pais] = []
            dicc[pais].append(nombre)
    archivo.close()
    return dicc

# print(filtrar("inmigrantes.txt",2019))


def contar_ingresos(nombre_archivo, año):
    paises = filtrar(nombre_archivo, año)
    retorno = {}
    for pais in paises:
        retorno[pais] = len(paises[pais])
    return retorno


def escribir_ingresos(nombre_archivo, año):
    paises = contar_ingresos(nombre_archivo, año)
    lista = []
    total = 0
    for pais in paises:
        lista.append((paises[pais], pais))
        total += paises[pais]
    lista.sort()
    lista.reverse()

    nomarch = "ingresos{}.txt"
    archivo = open(nomarch.format(año), "w")
    i = 1

    formato = "{}-{}:{}\n"

    while i < len(lista) + 1:
        archivo.write(formato.format(i, lista[i - 1][1], lista[i - 1][0]))
        i += 1
    archivo.close()
    return total

# print(escribir_ingresos('inmigrantes.txt',2018))

# C2 2020-1


def Filtrar(nombre_archivo, consola, minima):
    archivo = open(nombre_archivo)
    nombre_f = "{}.txt"
    salida = open(nombre_f.format(consola), "w")
    formato = "{} ({}), de {} ({}), con nota: {}.\n"
    cont = 0
    for linea in archivo:
        nombre, _, generos, dist, nota, _, plataforma, _, año = linea.strip().split(";")
        if int(nota) >= minima and plataforma == consola:
            salida.write(formato.format(nombre, generos, dist, año, nota))
            cont += 1
    archivo.close()
    salida.close()
    return cont

# print(Filtrar('juegos.txt','X360',90))


def rankear(nombre_archivo):
    archivo = open(nombre_archivo)
    diccionario = {}  # {Action: [(nota1,"titulo1","plataforma1"),(),()]}
    for linea in archivo:
        titulo, _, generos, _, nota, _, plataforma, _, _ = linea.strip().split(";")
        generos = generos.split(",")
        for genero in generos:
            if genero not in diccionario:
                diccionario[genero] = []
            diccionario[genero].append((nota, titulo, plataforma))
    archivo.close()

    nom_f = "{}.txt"
    formato = " {} ({})\n"
    for genero in diccionario:
        diccionario[genero].sort()
        diccionario[genero].reverse()
        salida_genero = open(nom_f.format(genero), "w")
        salida_genero.write(genero + "\n")
        for nota, titulo, plataforma in diccionario[genero][:3]:
            salida_genero.write(formato.format(titulo, plataforma))
        salida_genero.close()
    return len(diccionario)


print(rankear("juegos.txt"))
