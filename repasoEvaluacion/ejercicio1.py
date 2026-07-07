class MiPila:

    def __init__(self):
        self.pila = []

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if not self.pila:
            print("No hay elementos")
            return False
        return self.pila.pop()

    def verTope(self):
        if self.pila is None:
            print("La pila esta vacia")
            return None
        return self.pila[-1]
    
pila = MiPila()

#pila.apilar(4)
pila.apilar(7)
print(pila.desapilar)
print(pila.verTope)



