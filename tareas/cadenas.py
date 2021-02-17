def valida(cadena):
    i = 0
    bases = "ACGT "
    while i < len(cadena):
        if cadena[i] in bases:
            i += 1
        else:
            return False
    return True


X = "ACGT"
print(valida(X))
