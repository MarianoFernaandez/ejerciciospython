"""Que es una lista circular?"""

"""

Idea clave: En una lista circular el ultimo apunta al primero. 
    - No hay none al final; hay ciclo.

"""

#Definir el nodo

class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#Definir la Lista Circular

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    #Metodo para agregar elementos

    def agregar (self, dato):
        nuevo = NodoCircular(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    #Metodo para Mostrar (Cuantas veces quiero que se repita)

    def mostrar (self, pasos=10):
        actual = self.cabeza
        cont = 0
        while actual and cont < pasos:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            cont += 1
        print("...(Ciclica)")

    #Metodo para mostrar Lista Completa

    def mostrarCompleto (self):
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            print(actual.dato, end = " -> ")
            actual = actual.siguiente
        print(actual.dato)

    #Metodo Buscar

    def buscar (self, dato):
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            return False
        
    #Metodo Eliminar

    def eliminar (self, dato):

        if not self.cabeza:
            return False
        
        actual = self.cabeza

        #CASO CABEZA: El nodo a eliminar es la CABEZA

        if actual.dato == dato:
            print(f"El dato {dato} (Cabeza) se encontro y se eliminara")

            # PASO 1: Encontrar al último nodo (El explorador camina)
            ultimo = self.cabeza 
            while ultimo.siguiente != self.cabeza:
                ultimo = ultimo.siguiente # Esto es CAMINAR (avanzar al siguiente nodo)

            # PASO 2: Nombrar a la nueva cabeza (Beto)
            self.cabeza = actual.siguiente

            # PASO 3: El último (Carlos) suelta a Ana y agarra a la nueva cabeza
            ultimo.siguiente = self.cabeza

            return True
        
        #CASO GENERAL: El nodo a eliminar está en el medio o es el último

        anterior = actual
        actual = actual.siguiente

        while actual != self.cabeza:
            if actual.dato == dato:
                print(f"El dato {dato} se encontro y se eliminara")
                anterior.siguiente = actual.siguiente
                return True
            


        

            anterior = actual
            actual = actual.siguiente

        return False


def iniciar_menu():
    lc = ListaCircular()


    for c in ("A", "B", "C", "D"):
        lc.agregar(c)

    
    while True:
        print("\n" + "="*30)
        print("    MENÚ DE LISTA ENLAZADA")
        print("="*30)
        print("1. Agregar un elemento") #CONFIRMADO
        print("2. Mostrar en repeticiones") #CONFIRMADO
        print("3. Mostrar Completo") #CONFIRMADO
        print("4. Buscar") #CONFIRMADO
        print("5. Eliminar") 
        print("6. Actualizar")
        print("7. Salir")
        print("="*30)
        
        opcion = input("Elige una opción (1-7):")
        
        if opcion == '1':
            dato = input("Ingresa el dato a insertar: ")
            lc.agregar(dato)
            print(f"✅ '{dato}' ha sido insertado.")
        
        elif opcion == "2":
            print()
            lc.mostrar()
            
        elif opcion == "3":
            print()
            lc.mostrarCompleto()

        elif opcion == "4":
            dato = input("Ingresa el dato que quieres buscar: ")
            if lc.buscar(dato):
                print()
                print(f"El elemento '{dato}' SÍ esta en la lista.")
            else:
                print()
                print(f"El elemento '{dato}' NO se encontro")
        
        elif opcion == "5":
            dato = input("Ingresa el dato a eliminar: ")
            if lc.eliminar(dato):
                print()
                print(f"'{dato}' fue eliminado")
            else:
                print()
                print(f"No se pudo eliminar. '{dato}' no esta en la lista")

        elif opcion == "6":
            viejo = input("Ingresa el dato que quieras cambiar: ")
            nuevo = input("Ingresa el dato nuevo: ")
            if lc.actualizar(viejo, nuevo):
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

