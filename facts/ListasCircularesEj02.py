class Persona:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None
    
    def agregar_persona(self, dato):
        p = Persona(dato)
        if not self.cabeza:
            self.cabeza=p
            p.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = p
            p.siguiente = self.cabeza

def josephus(n ,k):
        l = ListaCircular()
        for i in range(1 , n+1):
            l.agregar_persona(i)
        
        actual = l.cabeza
        anterior = None
        
        while actual.siguiente != actual:
            for i in range(k-1):
                anterior = actual
                actual = actual.siguiente
        
            print(f"se elmino {actual.dato}")
            anterior.siguiente = actual.siguiente
            actual = actual.siguiente
        return print(f"Quedo el numero: {actual.dato}")
    
josephus(7,3)
    

    
    
    


        



        