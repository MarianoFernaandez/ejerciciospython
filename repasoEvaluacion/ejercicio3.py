def producto(lista):
    if lista is None:
        return 1
    return lista[0] * producto(lista[1:])

print(producto([3,5]))