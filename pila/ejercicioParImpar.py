"""

Una pila o stack es una estructura de datos que sigue 
la regla de LIFO(Last In, First Out): es decir, el 
ultimo elemento que entra es el primero en salir. 

Operaciones Basicas: 
1- Push(apilar) -> Insertar un elemento arriba.
2- Pop(desapilar) -> Sacar el elemento superior (de arriba)
3- Peek(mirar el tope) -> Ver el elemento superior sin quitarlo
4- isEmpty -> saber si la pila esta vacia

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

pilaPrincipal = Pila()
pilaPares = Pila()
pilaImpares = Pila()

print("Ingresa números para la pila (ingresa 0 para terminar).")

while True:

    numeroIngresado = int(input("Ingrese un numero: "))

    if numeroIngresado == 0:
        break

    pilaPrincipal.push(numeroIngresado)

print("Pila Principal antes de separar")
pilaPrincipal.mostrar()

while not pilaPrincipal.esta_vacia():

    numeroActual = pilaPrincipal.pop()

    if numeroActual % 2 == 0:
        pilaPares.push(numeroActual)
    else:
        pilaImpares.push(numeroActual)

print()

print("Pila Impares")
pilaImpares.mostrar()

print("Pila Par")
pilaPares.mostrar()