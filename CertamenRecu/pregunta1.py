def min_max(nombre_archivo, pais):
    archivo = open(nombre_archivo)
    lista1 = []
    lista2 = []
    lista3 = []
    for linea in archivo:
        ano, ciudad, pais2, poblacion, _ = linea.strip().split(",")
        if pais == pais2:
            lista1.append((int(poblacion), int(ano), ciudad))
    lista1.sort()
    for elemento in lista1:
        poblacion2, ano2, ciudad2 = elemento
        if ciudad2 not in lista2:
            lista2.append(ciudad2)
    for elemento2 in lista2:
        lista4 = list()
        for ciudades in lista1:
            poblacion3, ano3, ciudad3 = ciudades
            if elemento2 == ciudad3:
                lista4.append((poblacion3, ano3))
        pob_min = lista4[0][0] 
        pob_max = lista4[-1][0]
        ano_min = lista4[0][1]
        ano_max = lista4[-1][1]
        lista3.append((elemento2, ano_min, pob_min, ano_max, pob_max))
    archivo.close()
    return lista3


print(min_max('ciudades.txt', 'United States'))
