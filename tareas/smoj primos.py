a = int(input())
b = int(input())
veces = b - a
i = 0
div = 2
primo = True
suma = 0
while i <= veces:
    while div < (a + i) / 2:
        if (a + i) % div == 0:
            primo = False
        div += 1
    if primo:
        suma += (a + i)
    i += 1
