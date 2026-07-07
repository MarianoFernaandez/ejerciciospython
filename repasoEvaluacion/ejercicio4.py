class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def __str__(self):
        return self.dato

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def __str__(self):
        respuesta=""
        actual = self.cabeza
        while actual.siguiente is not None:
            respuesta = respuesta + actual.dato + " -> "
            actual= actual.siguiente
        respuesta = respuesta + actual.dato + " -> "
        return respuesta + "none"

    def agregar(self, dato):
        nodoNuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodoNuevo
            return
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual= actual.siguiente
            actual.siguiente = nodoNuevo

    def eliminar(self, elemento):
        if self.cabeza.dato == elemento:
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            while (actual.dato != elemento):
                anterior = actual
                actual = actual.siguiente
            anterior.siguiente = actual.siguiente

    def buscar(self, elemento):
        if self.cabeza.dato == elemento:
            return self.cabeza
        else:
            actual = self.cabeza
            while (actual.dato != elemento and actual.dato != None):
                actual = actual.siguiente
                
                if actual.dato is None:
                    return ("No esta el numero que buscas") 
                
                return actual.dato
        
            



lista = ListaEnlazada()
lista.agregar("5")
lista.agregar("7")
lista.agregar("5")
lista.agregar("7")
print(lista)
lista.eliminar("7")
lista.eliminar("5")
print(lista)
print(lista.buscar("5"))
print(lista.buscar("7"))
print(lista.buscar("9"))




        



