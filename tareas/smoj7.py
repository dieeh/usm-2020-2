original = [1, 2, 3, 1, 2, 3, 1, 2, 3]
eliminar = ['peras', 1, 2]


def filtrar(original, eliminar):
    if original == []:
        return []
    i = 0
    if eliminar[i] not in original:
        eliminar.remove(eliminar[i])
    while i < len(eliminar):
        flag = True
        while flag:
            original.remove(eliminar[i])
            if eliminar[i] not in original:
                flag = False
        i += 1
    w = []
    j = 0
    while j < len(original):
        if original[j] not in w:
            w.append(original[j])
        j += 1
    return w


a = filtrar(original, eliminar)
print(a)
