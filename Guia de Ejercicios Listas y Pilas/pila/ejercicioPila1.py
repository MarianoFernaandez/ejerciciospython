# ---------------------------------------------------------------------------
# EJERCICIO 01: Navegador web: atrás y adelante
# [AUTOR: GEMINI]
# ENUNCIADO: Usa dos pilas. Al visitar página nueva la pila adelante se vacía.
# ---------------------------------------------------------------------------
class PilaNavegador:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if not self.esta_vacia() else None
    def peek(self): return self.items[-1] if not self.esta_vacia() else None
    def esta_vacia(self): return len(self.items) == 0
    def vaciar(self): self.items = []

class NavegadorPilas:
    def __init__(self):
        self.atras_pila = PilaNavegador()
        self.adelante_pila = PilaNavegador()

    def visitar(self, url):
        self.atras_pila.push(url)
        self.adelante_pila.vaciar()

    def atras(self):
        if not self.atras_pila.esta_vacia():
            actual = self.atras_pila.pop()
            self.adelante_pila.push(actual)
            return self.atras_pila.peek()
        return None

    def adelante(self):
        if not self.adelante_pila.esta_vacia():
            siguiente = self.adelante_pila.pop()
            self.atras_pila.push(siguiente)
            return siguiente
        return None
    
# ---------------------------------------------------------------------------------------

print("--- Inicializando el Navegador Web ---")
nav = NavegadorPilas()

# 1. Visitamos un par de páginas en orden
print("\nVisitando páginas...")
nav.visitar("google.com")
print(f"Página actual: {nav.atras_pila.peek()}")

nav.visitar("youtube.com")
print(f"Página actual: {nav.atras_pila.peek()}")

nav.visitar("github.com")
print(f"Página actual: {nav.atras_pila.peek()}")

# 2. Presionamos el botón "Atrás" dos veces
print("\n--- Navegando hacia Atrás ---")
print(f"Click 'Atrás' -> Ahora viendo: {nav.atras()}") # Debería ser youtube.com
print(f"Click 'Atrás' -> Ahora viendo: {nav.atras()}") # Debería ser google.com

# 3. Presionamos el botón "Adelante" una vez
print("\n--- Navegando hacia Adelante ---")
print(f"Click 'Adelante' -> Ahora viendo: {nav.adelante()}") # Debería ser youtube.com

# 4. Visitamos una nueva página (esto borra el "futuro" que era github.com)
print("\n--- Visitando nueva página (Borra historial futuro) ---")
nav.visitar("stackoverflow.com")
print(f"Página actual: {nav.atras_pila.peek()}")

# 5. Intentamos ir "Adelante" nuevamente
print("\n--- Intentando ir Adelante ---")
siguiente = nav.adelante()
if siguiente is None:
    print("El botón 'Adelante' está deshabilitado (No hay páginas futuras).")
else:
    print(f"Click 'Adelante' -> Ahora viendo: {siguiente}")