seg = int(input("Ingrese la cantidad de segundos: "))
mins = seg//60
seg = seg%60
hrs = mins//60
mins = mins%60

print(hrs,"horas",mins,"minutos y",seg,"segundos")
