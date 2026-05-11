class Paciente:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def ingresar_paciente(self, nombre, prioridad):
        nuevo = Paciente(nombre, prioridad)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            if nuevo.prioridad < self.cabeza.prioridad:
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
                nuevo.siguiente.anterior = nuevo
                return
            while actual.siguiente is not None and actual.siguiente.prioridad < nuevo.prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
            if nuevo.siguiente is not None :
                nuevo.siguiente.anterior = nuevo
                


    def atender(self):
        if self.cabeza is None:
            print("No hay nadie en lista!")
        else:
            p = self.cabeza.nombre
            self.cabeza = self.cabeza.siguiente
            return p
        
    def mostrar_sala(self):
        inicio = self.cabeza
        while inicio is not None:
            print(inicio.nombre)
            inicio = inicio.siguiente

    def reasignar_prioridad(self, nombre, prioridadN):
        actual = self.cabeza
        while actual is not None and actual.nombre != nombre:
            actual = actual.siguiente
        
        if actual is None:
            print("El paciente No existe!")
            return

        if actual.anterior is None:
            self.cabeza = actual.siguiente
            if actual.siguiente is not None:
                actual.siguiente.anterior = None
        elif actual.siguiente is  None:
            actual.anterior.siguiente = None
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        actual.prioridad = prioridadN

        self.ingresar_paciente(actual.nombre, actual.prioridad)


l = ListaEnlazada()

l.ingresar_paciente("luis",1)
l.ingresar_paciente("carlos",2)
l.ingresar_paciente("ana", 5)
l.ingresar_paciente("valentin",3)
l.ingresar_paciente("cacorro",1)
l.mostrar_sala()
l.atender()
l.mostrar_sala()
l.ingresar_paciente("luisito",1)
l.mostrar_sala()
            



