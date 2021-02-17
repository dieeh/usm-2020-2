from typing import Dict, List, Any


def separar(nombre_archivo, rubro, ano):
    lista = []
    lista2 = []
    diccionario: dict[Any, list[Any]] = dict()
    archivo_marcas = open(nombre_archivo,'r')
    for x in archivo_marcas:
        campo = x.strip().split(',')
        lista.append(campo)
    for elemento in lista:
        fecha, marca, pais, valor, rubro2 = elemento
        ano2, mes, dia = fecha.split('-')
        if ano == ano2 and rubro == rubro2:
            lista2.append([valor, marca, pais])
    lista2.sort()
    lista2.reverse()
    for variables in lista2:
        valor2, marca2, pais2 = variables
        if pais2 not in diccionario:
            diccionario[pais2] = []
        diccionario[pais2] += ((marca2, valor2))
    archivo_marcas.close()
    return diccionario


a = separar('marcas.txt','Fast-Moving Consumer Goods','2016')
print(a)