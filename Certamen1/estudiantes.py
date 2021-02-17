def suma_productos(rut):
    suma_n = 0
    i = 2  # constante a multiplicar, comenzando por la derecha: 2, 3, 4, 5, 6, 7, 1, 2
    while rut != 0:
        n = rut % 10      # obtiene el dígito de mas a la derecha
        rut = rut // 10   # elimina el dígito de mas a la derecha
        suma_n += n * i
        # A continuación, se actualiza la constante para la siguiente iteración
        i += 1
        if i == 8:    # después del 7, vuelve a 2
            i = 2
    return suma_n
