class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.der, valor)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izq)
            print(nodo.valor, end=' ')
            self.inorden(nodo.der)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.valor, end=' ')

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izq, valor)
        else:
            return self._buscar_recursivo(nodo.der, valor)        
        
    def contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        else:
            return self.contar_hojas(nodo.izq) + self.contar_hojas(nodo.der)    
        
    def altura(self, nodo):
            if nodo is None: 
                return 0
            else:
                altura_izq = self.altura(nodo.izq)
                altura_der = self.altura(nodo.der)
                return max(altura_izq, altura_der) + 1

    def factor_de_balance(self, nodo):
        if nodo is None:
            return 0
        altura_izq = self.altura(nodo.izq)
        altura_der = self.altura(nodo.der)
        return altura_izq - altura_der        
            
arbol = ArbolBinario()
arbol.insertar('F')
arbol.insertar('B')
arbol.insertar('G')
arbol.insertar('A')
arbol.insertar('D')
arbol.insertar('C')
arbol.insertar('E') 

arbol.buscar('D')
