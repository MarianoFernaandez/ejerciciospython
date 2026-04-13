class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    ######## READ ########
    def buscar (self,dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    ######## UPDATE ########
    def actualizar (self, viejo, nuevo):
        actual = self.cabeza
        while actual:
            if actual.dato == viejo:
                actual.dato = nuevo
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente

    def esta_vacia(self):
        return self.cabeza is None

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos)

# --- SISTEMA DE MENÚ ---
def iniciar_menu():
    l = ListaEnlazada()
    
    while True:
        print("\n" + "="*30)
        print("    MENÚ DE LISTA ENLAZADA")
        print("="*30)
        print("1. Insertar un elemento")
        print("2. Buscar un elemento")
        print("3. Actualizar un elemento")
        print("4. Eliminar un elemento")
        print("5. Mostrar la lista")
        print("6. Ver si la lista está vacía")
        print("7. Salir")
        print("="*30)
        
        opcion = input("Elige una opción (1-7): ")
        
        if opcion == '1':
            dato = input("Ingresa el dato a insertar: ")
            l.insertar(dato)
            print(f"✅ '{dato}' ha sido insertado.")
            
        elif opcion == '2':
            dato = input("Ingresa el dato que quieres buscar: ")
            if l.buscar(dato):
                print(f"✅ El elemento '{dato}' SÍ está en la lista.")
            else:
                print(f"❌ El elemento '{dato}' NO se encontró.")
                
        elif opcion == '3':
            viejo = input("Ingresa el dato actual (viejo) a reemplazar: ")
            nuevo = input("Ingresa el dato nuevo: ")
            if l.actualizar(viejo, nuevo):
                print(f"✅ Se actualizó '{viejo}' por '{nuevo}'.")
            else:
                print(f"❌ No se encontró '{viejo}' en la lista.")
                
        elif opcion == '4':
            dato = input("Ingresa el dato a eliminar: ")
            if l.eliminar(dato):
                print(f"✅ '{dato}' ha sido eliminado.")
            else:
                print(f"❌ No se pudo eliminar. '{dato}' no está en la lista.")
                
        elif opcion == '5':
            print("\nContenido de la lista:")
            print(l)
            
        elif opcion == '6':
            if l.esta_vacia():
                print("✅ La lista SÍ está vacía.")
            else:
                print("❌ La lista NO está vacía.")
                
        elif opcion == '7':
            print("¡Hasta luego! Saliendo del programa...")
            break
            
        else:
            print("⚠️ Opción no válida. Por favor, elige un número del 1 al 7.")

# Ejecutamos el menú
if __name__ == "__main__":
    iniciar_menu()