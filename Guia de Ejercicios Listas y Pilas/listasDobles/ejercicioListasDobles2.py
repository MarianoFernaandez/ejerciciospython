class NodoAccion:
    def __init__(self, accion):
        self.accion = accion
        self.siguiente = None
        self.anterior = None

class UndoRedo:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def ejecutar(self, accion):
        nuevo = NodoAccion(accion)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.actual = nuevo
        else:
            self.actual.siguiente = nuevo
            nuevo.anterior = self.actual
            self.actual = nuevo

    def undo(self):
        if self.actual and self.actual.anterior:
            accion_deshecha = self.actual.accion
            self.actual = self.actual.anterior
            return accion_deshecha
        return None

    def redo(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.accion
        return None

    def historial(self):
        nodo = self.cabeza
        while nodo:
            marca = "[ACTUAL]" if nodo == self.actual else ""
            print(f"{nodo.accion} {marca}")
            nodo = nodo.siguiente

# -------------------------------------------------------------------------------

print("--- Inicializando el Sistema Undo/Redo ---")
ur = UndoRedo()

# 1. Ejecutamos un par de acciones iniciales
ur.ejecutar("Escribir 'Hola'")
ur.ejecutar("Escribir ' Mundo'")
ur.ejecutar("Aplicar formato 'Negrita'")

print("\nHistorial tras ejecutar 3 acciones:")
ur.historial()

# 2. Deshacemos (Undo) las últimas dos acciones
print("\n--- Haciendo Undo dos veces ---")
ur.undo()
ur.undo()
ur.historial()

# 3. Rehacemos (Redo) una acción
print("\n--- Haciendo Redo una vez ---")
ur.redo()
ur.historial()

# 4. Ejecutamos una nueva acción (Esto debe borrar el futuro/Redo restante)
print("\n--- Ejecutando nueva acción (Debe borrar el futuro) ---")
ur.ejecutar("Aplicar formato 'Cursiva'")
ur.historial()