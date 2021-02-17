artistas = [
    ('Troye Mars', 'Rock', 150232, (1996, 10, 8)),
    ('Destiny Cyrus', 'Hip-Hop', 973923, (1989, 11, 21)),
    ('Enrique Morales', 'Pop', 200343, (1993, 4, 26)),
    ('Bruno Eilish', 'Pop Electronico', 782140, (2001, 2, 12)),
    ('Onika Maraj', 'Pop', 196222, (1967, 7, 13)),
    ('Britney Perry', 'Pop', 1234980, (1981, 12, 24))
]


def generos_con_mas_seguidores(artistas):
    k = {}
    h = []
    g = []
    i = 0
    while i < len(artistas):
        if artistas[i][1] not in k:
            k[artistas[i][1]] = artistas[i][2]
        else:
            k[artistas[i][1]] += artistas[i][2]
        i += 1
    for genero in k:
        h.append([k[genero], genero])
    h.sort()
    h.reverse()
    for lista in h[0:3]:
        g.append(lista[1])
    return g


# k = {'Rock':150232, 'Hip-Hop':973923, 'Pop':1631545, 'Pop Electronico':782140}
a = generos_con_mas_seguidores(artistas)
print(a)
