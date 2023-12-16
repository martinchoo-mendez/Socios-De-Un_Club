def buscar (lista, entero):
    for i in range(len(lista)):
        if lista[i]==entero:
            return i
    return -1