"""

Dada 3 pilas con numeros ordenados de menor a 
mayor, armar una con todos los datos ordenados.

"""

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, dato): 
        self.elementos.append(dato)

    def pop(self):
        if not self.esta_vacia():
            # 👇 AQUÍ SE CORRIGIÓ EL ERROR: Se agregaron los paréntesis () 
            return self.elementos.pop()
        return None
    
    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def mostrar(self):
        print(self.elementos)


# 1. Creamos las pilas
primerPila = Pila()
segundaPila = Pila()
tercerPila = Pila()

# 2. Cargamos las pilas

primerPila.push(7)
primerPila.push(3)
primerPila.push(1)

segundaPila.push(5)
segundaPila.push(4)
segundaPila.push(2)

tercerPila.push(9)
tercerPila.push(8)
tercerPila.push(6)

pilaPrincipal = Pila()

while not primerPila.esta_vacia() or not segundaPila.esta_vacia() or not tercerPila.esta_vacia():

    valorUno = 999
    valorDos = 999
    valorTres = 999
    

    if not primerPila.esta_vacia():
        valorUno = primerPila.peek()

    if not segundaPila.esta_vacia():
        valorDos = segundaPila.peek()

    if not tercerPila.esta_vacia():
            valorTres = tercerPila.peek()

    #Extraer la pila menor

    if valorUno <= valorDos and valorUno <= valorTres:
        numeroExtraido = primerPila.pop()

    elif valorDos <= valorUno and valorDos <= valorTres:
        numeroExtraido = segundaPila.pop()

    else:
        numeroExtraido = tercerPila.pop()
        
    pilaPrincipal.push(numeroExtraido)

    print(f"Topes: {valorUno}, {valorDos}, {valorTres} | Extraído: {numeroExtraido}")

print("\n¡Fusión completada en pila principal!")
pilaPrincipal.mostrar()

            
    

    

