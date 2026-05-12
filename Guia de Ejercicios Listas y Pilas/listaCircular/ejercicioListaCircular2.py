class Persona:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircularJosephus:
    def __init__(self):
        self.cabeza = None
    
    def agregar_persona(self, dato):
        p = Persona(dato)
        if not self.cabeza:
            self.cabeza = p
            p.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = p
            p.siguiente = self.cabeza

def josephus(n, k):
    l = ListaCircularJosephus()
    for i in range(1, n+1):
        l.agregar_persona(i)
    
    actual = l.cabeza
    anterior = None
    
    while actual.siguiente != actual:
        for _ in range(k-1):
            anterior = actual
            actual = actual.siguiente
        
        anterior.siguiente = actual.siguiente
        actual = actual.siguiente
        
    return actual.dato

# ----------------------------------------------------------------------------------------------------

print("--- Inicializando Simulación de Josephus ---")

# Caso de prueba 1: El del PDF
n1, k1 = 7, 3
print(f"\nSimulando con N={n1} personas en círculo.")
print(f"Eliminando de a K={k1} posiciones...")
sobreviviente1 = josephus(n1, k1)
print(f"¡El sobreviviente es la persona número: {sobreviviente1}! (Esperado: 4)")
