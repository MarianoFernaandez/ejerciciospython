class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class Buffer:
    def __init__(self, capacidad):
        self.cabeza = None
        self.capacidad = capacidad
        self.puntero = None
        self.iniciarBufer(capacidad)

    def iniciarBufer(self, n):
        for i in range(n):
            nuevo = Nodo(None)
            if self.cabeza is None:
                self.cabeza = nuevo
            else:  
                actual = self.cabeza
                while actual.siguiente is not None:
                    actual = actual.siguiente
                actual.siguiente = nuevo
        nuevo.siguiente = self.cabeza
        self.puntero = self.cabeza
    
    def registrar(self, mensaje):
        self.puntero.dato = mensaje
        self.puntero = self.puntero.siguiente
    
    def mostrar_logs(self):
        aux = self.puntero
        while True:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.puntero:
                break

b = Buffer(4)
b.registrar("mensaje 1")
b.registrar("mensaje 2")
b.registrar("mensaje 3")
b.registrar("mensaje 4")
b.mostrar_logs()       


