from funciones import *

numero = int(input("Ingrese un número entero mayor que uno: "))
while numero <= 1:
    numero = int(input("Ingrese un número entero mayor que uno: "))
if primo(numero):
    print(numero, "es primo")
if primo_de_mersenne(numero):
    print(numero, "es primo de mersenne")
if numero_perfecto(numero):
    print(numero, "es perfecto")
if numero_narcisista(numero):
    print(numero, "es narcisista")

otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
while otro_numero <= 1:
    otro_numero = int(input("Ingrese otro número entero mayor que uno: "))
if primo(otro_numero):
    print(otro_numero, "es primo")
if primo_de_mersenne(otro_numero):
    print(otro_numero, "es primo de mersenne")
if numero_perfecto(otro_numero):
    print(otro_numero, "es perfecto")
if numero_narcisista(otro_numero):
    print(otro_numero, "es narcisista")

if son_amigos(numero, otro_numero):
    print(numero, "y", otro_numero, "son amigos")
