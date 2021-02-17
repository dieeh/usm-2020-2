d = float(input("Distancia: "))
a = float(input("Ángulo: "))
if d <= 7:
   print("Pileta")
elif d <= 20 or (d > 35 and d <= 47):
   if a >= 45 and a < 90:
      print("Público")
   else:
      print("Cemento")
elif d <= 35:
   if (a >= 135 and a < 180) or (a >= 225 and a < 270) or (a >= 315 and a < 360):
      print("Cemento")
   elif (a >= 45 and a < 90):
      print("Público")
   else:
      print("Área Verde")
else:
   print("Fuera de la plaza")
