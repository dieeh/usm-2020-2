"""
def camelCase(palabra):
    contador = 1
    i = 0
    while i < len(palabra):
        if palabra[i] in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            contador +=1
        i +=1
    return contador

pal = input()
print(camelCase(pal))
"""

'''
def ContienePyth(palabra):
    pyth = "pythonia"
    i = 0
    j = 0
    while i <= (len(palabra)-1) and j < 7:
        if palabra[i] == pyth[j]:
            j+=1
        i+=1
    if j == 7:
        return "SI"
    return "NO"

pal2 = input()
print(ContienePyth(pal2))
'''

'''
def espacios(m):
    i = 0
    pal = ""
    while i <= (len(m)-1):
        if m[i] == " ":
            i+=1
        pal += m[i]
            i+=1
    return pal


def palindromo(n):
    palabra = espacios(n)
    inverso = palabra[::-1]
    if palabra.lower() == inverso.lower():
        return "SI"
    return "NO"

pal3 = input()
print(palindromo(pal3))
'''


'''
def pangrama(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    contador = 0
    while i < len(abc):
        if abc[i] in palabra.lower():
            contador += 1
        i += 1
    if contador == len(abc) and len(palabra) > 0:
        return "PANGRAMA"
    else:
        return "NO PANGRAMA"


pal = input()
print(pangrama(pal))
'''
