class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    #---------------------
    #INSERTAR
    #---------------------

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo_actual):
        if dato <= nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(dato)
            else:
                self._insertar(dato, nodo_actual.izquierda)
        elif dato >= nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(dato)
            else:
                self._insertar(dato, nodo_actual.derecha)

    #---------------------
    #BUSCAR
    #---------------------

    def buscar(self, dato):
        return self._buscar(dato, self.raiz)

    def _buscar(self, dato, nodo_actual):
        if nodo_actual is None:
            return False
        if dato == nodo_actual.valor:
            return True
        elif dato < nodo_actual.valor:
            return self._buscar(dato, nodo_actual.izquierda)
        elif dato > nodo_actual.valor:
            return self._buscar(dato, nodo_actual.derecha)
        
    def contarHojas(self, nodo_actual):
        if nodo_actual is None:
                return 0
        if nodo_actual is not None:
            if nodo_actual.izquierda is None and nodo_actual.derecha is None:
                return 1
        return self.contarHojas(nodo_actual.izquierda) + self.contarHojas(nodo_actual.derecha)
        


    #---------------------
    #RECORRIDOS
    #---------------------

    #INORDEN

    def inorden(self):
        self._inorden(self.raiz, [])
        return self._inorden(self.raiz, [])

    def _inorden(self, nodo_actual, resultado):
        if nodo_actual:
            self._inorden(nodo_actual.izquierda, resultado)
            resultado.append(nodo_actual.valor)
            self._inorden(nodo_actual.derecha, resultado)
        return resultado

    #PREORDEN
    def preorden(self):
        self._preorden(self.raiz, [])
        return self._preorden(self.raiz, [])

    def _preorden(self, nodo_actual, resultado):
        if nodo_actual:
            resultado.append(nodo_actual.valor)
            self._preorden(nodo_actual.izquierda, resultado)
            self._preorden(nodo_actual.derecha, resultado)
        return resultado

    #POSTORDEN
    def postorden(self):
        self._postorden(self.raiz, [])
        return self._postorden(self.raiz, [])
    
    def _postorden(self, nodo_actual, resultado):
        if nodo_actual:
            self._postorden(nodo_actual.izquierda, resultado)
            self._postorden(nodo_actual.derecha, resultado)
            resultado.append(nodo_actual.valor)
        return resultado

# CARGA DE DATOS

arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("Recorrido PREORDEN: ", arbol.preorden())
print("Recorrido INORDEN: ", arbol.inorden())
print("Recorrido POSTORDEN: ", arbol.postorden())







# Insertar, buscar, calcular altura y hojas



