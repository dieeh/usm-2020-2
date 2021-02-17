'''
Busca el color indicado dentro de combinaciones y retorna un string con
los colores que lo componen, en el formato: color1+color2=color3.
En caso de no encontrar el color, retorna un string vacío.
combinaciones="amarillo+rojo=naranja;azul+amarillo=verde;..."
'''


def buscar_combinacion(combinaciones, color):
   combinaciones = combinaciones + ';'
   i = 0  # índice con que se recorre el string combinaciones
   j = 0  # se mantiene como el inicio de la definición de color actual
   while i < len(combinaciones):
      if combinaciones[i] == '=':
         # registra la posición donde comienza el nombre del color actual (al lado del igual)
         k = i + 1
         while combinaciones[i] != ';':
            # avanza hasta el final del nombre del color actual (al encontrar ;)
            i += 1
         if combinaciones[k:i] == color:
            # hay coincidencia entre el color actual y el buscado
            return combinaciones[j:i]
         else:
            # no hay coincidencia, se procede con la siguiente definicion de color
            j = i + 1
      i += 1
   return ''  # llegamos al final sin encontrar el color, se retorna ''


'''
Agrega color al string resultado, siempre y cuando no exista previamente,
retornando el nuevo resultado.
Ejemplo de resultado: '−rojo−verde−amarillo'
'''


def agregar(resultado, color):
   # agrega guión para que el siguiente if considere el caso en que está al final
   nuevo_resultado = resultado + "-"
   if '-' + color + '-' in nuevo_resultado:
      # color ya está en resultado, se retorna sin cambios
      return resultado
   # como el color no estaba, se retorna el nuevo resultado con el color agregado al final
   return nuevo_resultado + color
