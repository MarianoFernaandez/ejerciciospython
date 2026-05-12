class NodoJugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class Juego:
    def __init__(self):
        self.cabeza = None
        self.turno_actual = None

    def agregar_jugador(self, nombre):
        nuevo = NodoJugador(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
            self.turno_actual = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def siguiente_turno(self):
        if not self.turno_actual: return None
        jugador = self.turno_actual.nombre
        self.turno_actual = self.turno_actual.siguiente
        return jugador

    def eliminar_jugador(self, nombre):
        if not self.cabeza: return
        actual = self.cabeza
        anterior = None
        while True:
            if actual.nombre == nombre:
                if actual.siguiente == actual: 
                    self.cabeza = None
                    self.turno_actual = None
                    return
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    ultimo = self.cabeza
                    while ultimo.siguiente != self.cabeza:
                        ultimo = ultimo.siguiente
                    self.cabeza = actual.siguiente
                    ultimo.siguiente = self.cabeza
                
                if self.turno_actual == actual:
                    self.turno_actual = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza: break

    def ganador(self):
        return self.cabeza.nombre if self.cabeza and self.cabeza.siguiente == self.cabeza else None
    
# -------------------------------------------------------------------------------------------------------

print("--- Inicializando el Juego de Mesa ---")
juego = Juego()

# 1. Agregamos jugadores a la ronda
juego.agregar_jugador("Ana")
juego.agregar_jugador("Beto")
juego.agregar_jugador("Carla")
juego.agregar_jugador("Diego")

print("\n--- Comienza la partida ---")
print(f"Turno 1: Juega {juego.siguiente_turno()}") 
print(f"Turno 2: Juega {juego.siguiente_turno()}") 
print(f"Turno 3: Juega {juego.siguiente_turno()}") 

# 2. Eliminamos a un jugador en el medio de la partida
print("\n--- ¡Carla ha sido eliminada del juego! ---")
juego.eliminar_jugador("Carla")

# 3. Seguimos rotando turnos (debería seguir Diego y luego volver a Ana)
print(f"Turno 4: Juega {juego.siguiente_turno()}") 
print(f"Turno 5: Juega {juego.siguiente_turno()}") 
print(f"Turno 6: Juega {juego.siguiente_turno()}") 

# 4. Eliminamos al resto hasta que quede un solo jugador
print("\n--- ¡Diego y Ana son eliminados! ---")
juego.eliminar_jugador("Diego")
juego.eliminar_jugador("Ana")

# 5. Comprobamos el ganador
ganador = juego.ganador()
if ganador:
    print(f"\n¡Tenemos un ganador! El último jugador en pie es: {ganador}")
else:
    print("\nNo hay ganador.")