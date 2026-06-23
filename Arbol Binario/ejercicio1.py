class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


#Cargo el arbol
raiz = Nodo('F')
raiz.izq = Nodo('B')
raiz.izq.izq = Nodo('A')
raiz.izq.der = Nodo('D')
raiz.izq.der.izq = Nodo('C')
raiz.izq.der.der = Nodo('E')
raiz.der = Nodo('G')
raiz.der.der = Nodo('I')
raiz.der.der.izq = Nodo('H')

#INORDEN

def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izq)
        print(nodo.valor, end=" - ")
        inorden(nodo.der)

#PREORDEN

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" - ")
        preorden(nodo.izq)
        preorden(nodo.der)

#POSTORDEN

def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=" - ")


#MUESTRA INORDEN

print("RESULTADO INORDEN")
inorden(raiz)
print()
print()

#MUESTRA PREORDEN

print("RESULTADO PREORDEN")
preorden(raiz)
print()
print()

#MUESTRA POSTORDEN

print("RESULTADO POSTORDEN")
postorden(raiz)








