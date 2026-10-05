class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

raiz = Nodo('F')
raiz.izq = Nodo('B')
raiz.der = Nodo('G')
raiz.izq.izq = Nodo('A')
raiz.izq.der = Nodo('D')
raiz.izq.der.izq = Nodo('C')
raiz.izq.der.der = Nodo('E')
raiz.der.der = Nodo('I')
raiz.der.der.izq = Nodo('H')

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=' ')
        preorden(nodo.izq)
        preorden(nodo.der)

print("\nRecorrido en preorden:\n")
preorden(raiz)

def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izq)
        print(nodo.valor, end=' ')
        inorden(nodo.der)

print("\nRecorrido en inorden:\n")
inorden(raiz)

def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=' ')

print("\nRecorrido en postorden:\n")
postorden(raiz)

def contar_nodos(nodo):
    if nodo is None:
        return 0
    else:
        return 1 + contar_nodos(nodo.izq) + contar_nodos(nodo.der)

print("\nNúmero de nodos en el árbol:\n")
print(contar_nodos(raiz))


def altura(nodo):
    if nodo is None:
        return 0
    else:
        altura_izq = altura(nodo.izq)
        altura_der = altura(nodo.der)
        return max(altura_izq, altura_der) + 1

print("\nAltura del árbol:\n")
print(altura(raiz))