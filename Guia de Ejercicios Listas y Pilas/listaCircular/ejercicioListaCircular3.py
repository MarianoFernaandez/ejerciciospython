# ---------------------------------------------------------------------------
# EJERCICIO 03: Buffer circular de logs del sistema
# [AUTOR: GEMINI]
# ENUNCIADO: Guarda N mensajes de log sobrescribiendo los antiguos.
# ---------------------------------------------------------------------------
class NodoLog:
    def __init__(self):
        self.mensaje = None
        self.siguiente = None

class RingBuffer:
    def __init__(self, capacidad):
        self.cabeza = NodoLog()
        actual = self.cabeza
        for _ in range(capacidad - 1):
            nuevo = NodoLog()
            actual.siguiente = nuevo
            actual = nuevo
        actual.siguiente = self.cabeza
        self.puntero_escritura = self.cabeza

    def registrar(self, mensaje):
        self.puntero_escritura.mensaje = mensaje
        self.puntero_escritura = self.puntero_escritura.siguiente

    def mostrar_logs(self):
        actual = self.puntero_escritura
        while True:
            if actual.mensaje is not None:
                print(actual.mensaje)
            actual = actual.siguiente
            if actual == self.puntero_escritura:
                break

# -----------------------------------------------------------------------------------------------

print("--- Inicializando Buffer Circular de Logs (Capacidad: 3) ---")
buffer = RingBuffer(3)

# 1. Registramos un par de eventos (el buffer aún tiene espacio)
buffer.registrar("Log 1: Sistema iniciado correctamente.")
buffer.registrar("Log 2: Usuario 'admin' ha iniciado sesión.")

print("\nEstado actual de los logs (Buffer con espacio):")
buffer.mostrar_logs()

# 2. Llenamos el buffer y forzamos la sobrescritura
print("\n--- Entrando en modo de alerta (Sobrescribiendo logs antiguos) ---")
buffer.registrar("Log 3: Conexión a la base de datos establecida.")
# Al ingresar el Log 4, la capacidad máxima (3) se supera. 
# Automáticamente se borrará el "Log 1"
buffer.registrar("Log 4: ADVERTENCIA - Latencia de red alta.") 
# Al ingresar el Log 5, se borrará el "Log 2"
buffer.registrar("Log 5: ERROR CRÍTICO - Pérdida de paquetes.")

# 3. Verificamos que los logs mantengan el orden cronológico correcto
print("\nEstado final de los logs (Solo deben verse del 3 al 5):")
buffer.mostrar_logs()