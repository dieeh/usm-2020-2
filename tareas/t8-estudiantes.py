# Nombre: Diego Eduardo Paz Letelier
# Paralelo: 211


personas = [
    ('Edsger Dijkstra', (1930, 5, 11), 'Holanda'),
    ('Alan Turing', (1912, 6, 23), 'Inglaterra'),
    ('Alonzo Church', (1903, 6, 14), 'Estados Unidos'),
    ('Stephen Cook', (1939, 12, 14), 'Estados Unidos'),
    ('Guido van Rossum', (1956, 1, 31), 'Holanda'),
    ('Tony Hoare', (1934, 1, 11), 'Inglaterra'),
    ('Grace Hopper', (1906, 12, 9), 'Estados Unidos'),
    ('Charles Babbage', (1791, 12, 26), 'Inglaterra'),
    ('Donald Knuth', (1938, 1, 10), 'Estados Unidos')
]


def misma_nacionalidad(personas, Nombre1, Nombre2):
    w = []
    i = 0
    j = 0
    while i < len(personas):
        if personas[i][0] == Nombre1:
            w.append(i)
        i += 1
    while j < len(personas):
        if personas[j][0] == Nombre2:
            w.append(j)
        j += 1
    if personas[w[0]][2] == personas[w[1]][2]:
        return True
    else:
        return False


def emparejar(personas, anno_i, anno_f):
    z = []
    i = 0
    while i < len(personas):
        anno, _, _ = personas[i][1]
        if anno_i <= anno <= anno_f:
            nombre1 = personas[i][0]
            j = 0
            while j < len(personas):
                anno2, _, _ = personas[j][1]
                if anno_i <= anno2 <= anno_f:
                    nombre2 = personas[j][0]
                    if nombre1 != nombre2:
                        k = misma_nacionalidad(personas, nombre1, nombre2)
                        if k and ((nombre2, nombre1, personas[i][2]) not in z):
                            z.append((nombre1, nombre2, personas[i][2]))
                j += 1
        i += 1
    return z


m = emparejar(personas, 1905, 1940)
print(m)
print(personas)

