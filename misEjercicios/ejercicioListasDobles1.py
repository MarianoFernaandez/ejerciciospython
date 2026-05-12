"""

Un editor de texto básico representa cada línea como un nodo. El cursor puede moverse hacia arriba o
abajo, insertar una línea nueva debajo del cursor y eliminar la línea actual.
Requerimientos:
• Cada nodo almacena el texto de una línea y punteros anterior y siguiente.
• Implementar cursor_arriba() y cursor_abajo(): mueven el puntero de posición.
• Implementar insertar_linea(texto): inserta después del cursor.
• Implementar eliminar_linea(): elimina la línea del cursor y mueve el cursor a la anterior (o siguiente si
    es la primera).
• Implementar mostrar(): imprime todas las líneas marcando cuál tiene el cursor con ».

"""

# Código base:
class NodoLinea:
    def __init__(self, texto):
        self.texto = texto
        self.siguiente = None
        self.anterior = None

class EditorTexto:
    def __init__(self):
        self.cabeza = None
        self.cursor = None 

    def insertar_linea(self, texto):
        nuevo = NodoLinea(texto)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cursor = nuevo
        else:
            nuevo.siguiente = self.cursor.siguiente
            nuevo.anterior = self.cursor
            
            if self.cursor.siguiente is not None:
                self.cursor.siguiente.anterior = nuevo
            
            self.cursor.siguiente = nuevo
            
            self.cursor = nuevo

    def eliminar_linea(self):
        if self.cursor is None: return
        
        aux = self.cursor
        # Puenteamos por arriba
        if aux.anterior:
            aux.anterior.siguiente = aux.siguiente
        else:
            self.cabeza = aux.siguiente
            
        # Puenteamos por abajo
        if aux.siguiente:
            aux.siguiente.anterior = aux.anterior
            
        # Movemos el cursor
        if aux.anterior:
            self.cursor = aux.anterior
        else:
            self.cursor = aux.siguiente

    def cursor_arriba(self):
        if self.cursor.anterior is None:
            print("No se puede ir para arriba, no hay nada")
            return
        else:
            self.cursor = self.cursor.anterior

    def cursor_abajo(self):
        if self.cursor.siguiente is None:
            print("No se puede ir para abajo, no hay nada")
        else:
            self.cursor = self.cursor.siguiente

    def mostrar(self):
        actual = self.cabeza

        while actual is not None:
            if actual == self.cursor:
                print(f">> {actual.texto}")
            else:
                print(f" {actual.texto}")

            actual = actual.siguiente   


mostrarNodo = EditorTexto()

mostrarNodo.insertar_linea("Hola, mi primer linea")
mostrarNodo.insertar_linea("Mi segunda linea")
mostrarNodo.insertar_linea("Mi tercer y ultima linea")



mostrarNodo.cursor_arriba()
mostrarNodo.cursor_arriba()

mostrarNodo.mostrar()