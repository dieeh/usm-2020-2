def numero_narcisista(n):
    i = 0
    """
    while n >= 10:
        n = n / 10
        i += 1
        return i
    """
    suma = 0
    while n > 0:
        digito = n % 10
        print(digito)
        n = n // 10
        suma += (digito ** i)
        print(suma)
    if suma == n:
        return True
    else:
        return False


numero = int(input())
print(numero_narcisista(numero))
