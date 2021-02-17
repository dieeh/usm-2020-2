def palindromo(n):
    numero = str(n)
    inverso = numero[::-1]
    if numero == inverso:
        return True
    else:
        return False


number = int(input())
palindromo = palindromo(number)

while palindromo == false:
