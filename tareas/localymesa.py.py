from funcionverificador import*


print("Datos del votante: ")
rut = str(input("Ingrese su rut con guion y digito verificador: "))
d = digito_verificador(int(rut[:-2]))
if d != int(rut[-1]):
    print("Rut invalido")
apellido = str(input("Ingrese sus apellidos: "))
a = apellido[0]
if a in "ABCDEFG":
    l = "Peumo"
elif a in "HIJKLMNÑO":
    l = "Quillay"
elif a in "PQRSTUVWXYZ":
    l = "Canelo"
nombre = str(input("Ingrese su nombre: "))
n = len(nombre)
n = n % 3 + 1


print("Le toca votar en la mesa", l, "-", n)
