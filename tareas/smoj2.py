Numero = int(input())
if (Numero // 100)**3 + ((Numero % 100) // 10)**3 + ((Numero % 100) % 10)**3 == Numero:
    Amstrong = True
else:
    Amstrong = False

if Amstrong:
    print("SI")
elif not Amstrong:
    print("NO")
