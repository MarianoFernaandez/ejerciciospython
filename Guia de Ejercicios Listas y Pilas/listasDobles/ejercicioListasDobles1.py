# ---------------------------------------------------------------------------
# EJERCICIO 01: Editor de texto con cursor
# [AUTOR: GEMINI]
# ENUNCIADO: El cursor puede moverse arriba/abajo, insertar línea y eliminar actual.
# ---------------------------------------------------------------------------
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
            if self.cursor.siguiente:
                self.cursor.siguiente.anterior = nuevo
            self.cursor.siguiente = nuevo
            self.cursor = nuevo

    def eliminar_linea(self):
        if self.cursor is None: return
        anterior = self.cursor.anterior
        siguiente = self.cursor.siguiente

        if anterior: anterior.siguiente = siguiente
        else: self.cabeza = siguiente
            
        if siguiente: siguiente.anterior = anterior
        self.cursor = anterior if anterior else siguiente

    def cursor_arriba(self):
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior

    def cursor_abajo(self):
        if self.cursor and self.cursor.siguiente:
            self.cursor = self.cursor.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            marca = "->" if actual == self.cursor else "  "
            print(f"{marca} {actual.texto}")
            actual = actual.siguiente

# ------------------------------------------------------------------------------

print("--- Inicializando el Editor de Texto ---")
editor = EditorTexto()

# 1. Insertamos un par de líneas
editor.insertar_linea("Línea 1: Hola Mundo")
editor.insertar_linea("Línea 2: Esto es un editor de texto")
editor.insertar_linea("Línea 3: Creado con Listas Doblemente Enlazadas")

print("\nEstado inicial (el cursor '->' debería estar en la última línea):")
editor.mostrar()

# 2. Movemos el cursor hacia arriba
print("\n--- Moviendo el cursor hacia arriba dos veces ---")
editor.cursor_arriba()
editor.cursor_arriba()
editor.mostrar()

# 3. Insertamos una línea en el medio
print("\n--- Insertando una nueva línea (Línea 1.5) ---")
editor.insertar_linea("Línea 1.5: ¡Me colé en el medio!")
editor.mostrar()

# 4. Eliminamos la línea actual
print("\n--- Eliminando la línea actual (la que tiene el cursor) ---")
editor.eliminar_linea()
editor.mostrar()

# 5. Movemos el cursor hacia abajo
print("\n--- Moviendo el cursor hacia abajo ---")
editor.cursor_abajo()
editor.mostrar()