edad = int(input("Ingresar edad: "))
altura = float(input("Ingresar altura en [cm]: "))
peso = float(input("Ingresar peso en [kg]: "))
mbh = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
mbm = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
imc = (peso / (altura * 0.01) ** 2)

print("Metabolismo Basal Hombres: ", round(mbh, 3))
print("Metabolismo Basal Mujeres: ", round(mbm, 3))
print("Índice de Masa Corporal: ", round(imc, 3))
