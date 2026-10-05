""""
Árbol AVL (Árbol Binario de Búsqueda auto-balanceado)
=======================================================

Implementación educativa que muestra cómo se detectan los desbalances
y cómo se aplican las 4 rotaciones (LL, RR, LR, RL) tanto al insertar
como al eliminar valores.

Autor: Jorge Polverini
"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1  # un nodo recién creado es una hoja -> altura 1


class ArbolAVL:
    # -----------------------------------------------------------------
    # Utilidades básicas
    # -----------------------------------------------------------------
    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _factor_balance(self, nodo):
        """FB = altura(izq) - altura(der). Debe estar en {-1, 0, 1}."""
        if nodo is None:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izquierda),
                               self._altura(nodo.derecha))

    # -----------------------------------------------------------------
    # Las 2 rotaciones simples (las dobles se arman combinándolas)
    # -----------------------------------------------------------------
    def _rotacion_derecha(self, z):
        r"""
        Caso LL: z está desbalanceado a la izquierda.
                z                y
               / \              / \
              y   T3    -->    x   z
             / \                  / \
            x   T2               T2 T3
        """
        y = z.izquierda
        T2 = y.derecha

        # Ejecutar la rotación
        y.derecha = z
        z.izquierda = T2

        # Actualizar alturas (primero el que quedó más abajo: z)
        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y  # y es la nueva raíz de este subárbol

    def _rotacion_izquierda(self, z):
        r"""
        Caso RR: z está desbalanceado a la derecha.
              z                    y
             / \                  / \
            T1  y       -->      z   x
               / \               / \
              T2  x             T1 T2
        """
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y

    # -----------------------------------------------------------------
    # Reequilibrar un nodo: decide cuál de los 4 casos aplica
    # -----------------------------------------------------------------
    def _reequilibrar(self, nodo):
        self._actualizar_altura(nodo)
        fb = self._factor_balance(nodo)

        # Caso izquierda pesada (FB > 1)
        if fb > 1:
            if self._factor_balance(nodo.izquierda) >= 0:
                # Caso LL -> una sola rotación derecha
                return self._rotacion_derecha(nodo)
            else:
                # Caso LR -> primero izquierda sobre el hijo, luego
                # derecha sobre el nodo (rotación doble)
                nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
                return self._rotacion_derecha(nodo)

        # Caso derecha pesada (FB < -1)
        if fb < -1:
            if self._factor_balance(nodo.derecha) <= 0:
                # Caso RR -> una sola rotación izquierda
                return self._rotacion_izquierda(nodo)
            else:
                # Caso RL -> primero derecha sobre el hijo, luego
                # izquierda sobre el nodo (rotación doble)
                nodo.derecha = self._rotacion_derecha(nodo.derecha)
                return self._rotacion_izquierda(nodo)

        # Ya estaba balanceado, no se hace nada
        return nodo

    # -----------------------------------------------------------------
    # Insertar
    # -----------------------------------------------------------------
    def insertar(self, raiz, valor):
        # 1. Inserción normal de BST
        if raiz is None:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self.insertar(raiz.derecha, valor)
        else:
            return raiz  # no se permiten valores duplicados

        # 2. Al volver de la recursión, reequilibrar este nodo
        #    (esto va corrigiendo el árbol desde la hoja hacia la raíz)
        return self._reequilibrar(raiz)

    # -----------------------------------------------------------------
    # Utilidades de visualización
    # -----------------------------------------------------------------
    def inorden(self, nodo, resultado=None):
        if resultado is None:
            resultado = []
        if nodo:
            self.inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self.inorden(nodo.derecha, resultado)
        return resultado

    def imprimir(self, nodo, prefijo="", es_izquierda=True):
        if nodo is not None:
            self.imprimir(nodo.derecha, prefijo + ("│   " if es_izquierda else "    "), False)
            print(prefijo + ("└── " if es_izquierda else "┌── ") + f"{nodo.valor} (FB={self._factor_balance(nodo)})")
            self.imprimir(nodo.izquierda, prefijo + ("    " if es_izquierda else "│   "), True)


# =======================================================================
# Demostración
# =======================================================================
if __name__ == "__main__":
    arbol = ArbolAVL()
    raiz = None

    # Insertamos 10, 20, 30 -> dispara una rotación izquierda simple (RR)
    valores = [10, 20, 30, 40, 50, 25]
    print("Insertando:", valores)
    for v in valores:
        raiz = arbol.insertar(raiz, v)

    print("\nÁrbol resultante:")
    arbol.imprimir(raiz)
    print("\nRecorrido inorden (debe salir ordenado):", arbol.inorden(raiz))