# ¿Qué es una lista doblemente enlazada?

"""
En la lista doblemente enlazada el nodo tiene:
-Dato y dos referencias: (1) Siguiente y (2) Anterior.
Ejemplo = Historial del navegador (Chrome)
CABEZA Y COLA
-Si guardas un puntero cabeza(primer nodo) puedes recorrer
hacia adelante.
- Si además guardamos un puntero a la cola(último), podemos
recorrer hacia atrás y, sobre todo, insertar al final
directamente sin recorrer toda la lista.
"""

#Definir el nodoDoble

class nodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

#Definir la listaDoble

class listaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

#Metodo Agregar

    def agregar(self, dato):
        nuevo = nodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

#Metodo Mostrar Adelante

    def mostrarAdelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    # [1, 2, 3] = 1 <-> 2 <-> 3 <-> None

#Metodo Mostrar Atras

    def mostrarAtras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")

    # [1, 2, 3] = 3 <-> 2 <-> 1 <-> None

#Metodo Buscar

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
#Metodo Eliminar

    def eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:

                if actual == self.cabeza and actual == self.cola:
                    self.cabeza = None
                    self.cola = None
                
                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                
                return True
            actual = actual.siguiente
        return False

#Metodo Actualizar

    def actualizar(self, viejo, nuevo):
        actual = self.cabeza
        while actual:
            if actual.dato == viejo:
                actual.dato = nuevo
                return True
            actual = actual.siguiente
        return False

# --- SISTEMA DE MENÚ ---
def iniciar_menu():
    l = listaDoble()

    for x in ("10", "20", "30", "40", "50"):
        l.agregar(x)
    
    while True:
        print("\n" + "="*30)
        print("    MENÚ DE LISTA ENLAZADA")
        print("="*30)
        print("1. Agregar un elemento") #CONFIRMADO
        print("2. Mostrar adelante") #CONFIRMADO
        print("3. Mostras atras") #CONFIRMADO
        print("4. Buscar") #CONFIRMADO
        print("5. Eliminar") #CONFIRMADO
        print("6. Actualizar")
        print("7. Salir")
        print("="*30)
        
        opcion = input("Elige una opción (1-7):")
        
        if opcion == '1':
            dato = input("Ingresa el dato a insertar: ")
            l.agregar(dato)
            print(f"✅ '{dato}' ha sido insertado.")
        
        elif opcion == "2":
            print()
            l.mostrarAdelante()
            
        elif opcion == "3":
            print()
            l.mostrarAtras()

        elif opcion == "4":
            dato = input("Ingresa el dato que quieres buscar: ")
            if l.buscar(dato):
                print()
                print(f"El elemento '{dato}' SÍ esta en la lista.")
            else:
                print()
                print(f"El elemento '{dato}' NO se encontro")
        
        elif opcion == "5":
            dato = input("Ingresa el dato a eliminar: ")
            if l.eliminar(dato):
                print()
                print(f"'{dato}' fue eliminado")
            else:
                print()
                print(f"No se pudo eliminar. '{dato}' no esta en la lista")

        elif opcion == "6":
            viejo = input("Ingresa el dato que quieras cambiar: ")
            nuevo = input("Ingresa el dato nuevo: ")
            if l.actualizar(viejo, nuevo):
                print(f"Se actualizo '{viejo}' por '{nuevo}'")
            else:
                print(f"No se encontro '{viejo}' en la lista.")

        elif opcion == '7':
            print("¡Hasta luego! Saliendo del programa...")
            break
            
        else:
            print("⚠️ Opción no válida. Por favor, elige un número del 1 al 7.")

# Ejecutamos el menú
if __name__ == "__main__":
    iniciar_menu()