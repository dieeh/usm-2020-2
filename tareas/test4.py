k = {'Rock': 150232,
     'Hip-Hop': 973923,
     'Pop': 1631545,
     'Pop Electronico': 782140}

h = []
g = []
for genero in k:
    h.append([k[genero], genero])
h.sort()
h.reverse()
for lista in h[0:3]:
    g.append(lista[1])

print(g)
