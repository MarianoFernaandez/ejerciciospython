# ---------------------------------------------------------------------------
# EJERCICIO 02: Cola de impresión con prioridad
# [AUTOR: Mariano]
# ENUNCIADO: Los trabajos "urgente" deben insertarse al inicio de la cola; 
# los normales al final.
# ---------------------------------------------------------------------------
class TrabajoImpresion:
    def __init__(self, usuario, doc, urgente=False):
        self.usuario = usuario
        self.doc = doc
        self.urgente = urgente
        self.siguiente = None

class ColaImpresion:
    def __init__(self):
        self.cabeza = None

    def agregar_trabajo(self, usuario, doc, urgente=False):
        nuevo = TrabajoImpresion(usuario, doc, urgente)
        if self.cabeza is None:
            self.cabeza = nuevo
            return

        if urgente:
            if not self.cabeza.urgente:
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                actual = self.cabeza
                while actual.siguiente and actual.siguiente.urgente:
                    actual = actual.siguiente
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def imprimir_siguiente(self):
        if self.cabeza is None:
            return "Cola vacía"
        trabajo = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return f"Imprimiendo: {trabajo.doc} de {trabajo.usuario}"

    def mostrar_cola(self):
        actual = self.cabeza
        while actual:
            tipo = "URGENTE" if actual.urgente else "Normal"
            print(f"[{tipo}] {actual.doc} ({actual.usuario})")
            actual = actual.siguiente

# ---------------------------------------------------------------------------

print("--- Inicializando la Cola de Impresión ---")
cola = ColaImpresion()

# 1. Agregamos un par de trabajos normales
cola.agregar_trabajo("Ana", "Reporte_Mensual.pdf")
cola.agregar_trabajo("Beto", "Fotos_Vacaciones.jpg")

print("\nEstado de la cola (solo normales):")
cola.mostrar_cola()

# 2. Llegan trabajos urgentes (deberían saltar al frente)
cola.agregar_trabajo("Jefe", "Contrato_Final.docx", urgente=True)
cola.agregar_trabajo("Carla", "Presentacion_Directorio.pptx", urgente=True)

# 3. Agregamos otro normal para ver que se va al fondo
cola.agregar_trabajo("Diego", "Receta_Cocina.txt")

print("\nEstado de la cola (urgentes saltaron al frente):")
cola.mostrar_cola()

# 4. Procesamos la impresión
print("\n--- Procesando impresión ---")
print(cola.imprimir_siguiente()) # Debería imprimir el del Jefe
print(cola.imprimir_siguiente()) # Debería imprimir el de Carla

print("\nEstado de la cola tras imprimir 2 documentos:")
cola.mostrar_cola()