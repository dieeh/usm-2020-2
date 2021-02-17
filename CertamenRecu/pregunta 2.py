def separar(nombre_archivo, rubro, anno):
    formato = "Mayor valor en {} de las marcas del rubro {}:\n"
    archivo = open(nombre_archivo)
    lista1 = []
    lista2 = []
    lista3 = []
    for linea in archivo:
        fecha, marca, pais, valor, rubro2 = linea.strip().split(",")
        ano, mes, dia = fecha.split("-")
        if ano == anno and rubro2 == rubro:
            lista2.append((int(valor), marca, pais, rubro2))
            if pais not in lista1:
                lista1.append(pais)
    lista2.sort()
    lista2.reverse()
    for paises in lista1:
        formato2 = "{}.txt"
        formato3 = "\tMarca: {}, valor en US$: {}\n"
        final = open(formato2.format(paises), "w")
        final.write(formato.format(anno, rubro))
        for elementos in lista2:
            valor2, marca2, pais2, rubro3 = elementos
            if pais2 == paises and marca2 not in lista3:
                valor_final = int(valor2) * 1000
                final.write(formato3.format(marca2, valor_final))
                lista3.append(marca2)
    archivo.close()
    final.close()
    return len(lista1)

a = separar('marcas.txt','Fast-Moving Consumer Goods','2016')
print(a)