'''
num1 = float(input("Escribe un número: "))
num2 = float(input("Escribe otro número: "))
num3 = float(input("Y otro más: "))
num4 = float(input("Uno más por si acaso: "))
oper = input("Y que deseas hacer con estos números?: ")

if oper == ["sumar", "suma", "+"]:
	print(num1 + num2 + num3 + num4)
elif oper == ^["restar", "resta", "-"]:
	print(num1 - num2 - num3 - num4)
elif oper == ["multiplicar","multiplicación","multiplicacion", "*"]:
	print(num1 * num2 * num3 * num4)
elif oper == ["dividir", "división", "division", "/"]:
	print(num1 / num2 / num3 / num4)
else:
	print("Operación invalida, prueba otra")
'''

num1 = float(input("Escribe un número: "))
num2 = float(input("Escribe otro número: "))
num3 = float(input("Y otro más: "))
num4 = float(input("Uno más por si acaso: "))
oper = input("Y que deseas hacer con estos números?: ")

if oper == "sum" or"sumar" or "suma" or "+":
	print(num1 + num2 + num3 + num4)
elif oper == "rest" or "restar" or "resta" or "-":
	print(num1 - num2 - num3 - num4)
elif oper == "mult" or "multiplicar" or "multiplicación" or "multiplicacion" or "*":
	print(num1 * num2 * num3 * num4)
elif oper == "div "or "dividir" or "división" or "division" or "/":
	print(num1 / num2 / num3 / num4)
else:
	print("Operación invalida, prueba otra")
