class NodoJugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class Juego:
    def __init__(self):
        self.primero = None
        self.turno = None  
        self.cantidad = 0   

    def agregarJugador(self, nombre): 
        nuevo = NodoJugador(nombre)

        if self.primero is None:
            self.primero = nuevo
            nuevo.siguiente = self.primero 
            self.turno = nuevo
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.siguiente = self.primero
        
        self.cantidad += 1

    def siguienteTurno(self):
        if self.turno:
            self.turno = self.turno.siguiente
            return self.turno.nombre
        return "No hay jugadores"

    def eliminarJugador(self, nombre): 
        if self.primero is None:
            print("No hay ningún jugador")
            return
        
        actual = self.primero
        anterior = None
        encontrado = False
        
        for _ in range(self.cantidad):
            if actual.nombre == nombre:
                encontrado = True
                break
            anterior = actual
            actual = actual.siguiente

        if not encontrado:
            print("Jugador no encontrado")
            return
        
        if self.cantidad == 1:
            self.primero = None
            self.turno = None
        elif actual == self.primero:
            ultimo = self.primero
            while ultimo.siguiente != self.primero:
                ultimo = ultimo.siguiente
            
            self.primero = actual.siguiente
            ultimo.siguiente = self.primero
        else:
            anterior.siguiente = actual.siguiente

        if actual == self.turno:
            self.turno = anterior if anterior else self.primero
            
        self.cantidad -= 1

    def hayGanador(self):
        return self.cantidad == 1
    
    def ganador(self):
        if self.hayGanador():
            return self.primero.nombre
        return "Todavía no hay un ganador único"

# ---------------------------------------------------------------------------------------------------

j = Juego()

for nombre in ["Ana", "Beto", "Carla", "Diego"]:
    j.agregarJugador(nombre)

print(f"Turno de: {j.siguienteTurno()}") 
print(f"Turno de: {j.siguienteTurno()}") 


print("\n--- Eliminando a Carla ---")
j.eliminarJugador("Carla")
print(f"Turno de: {j.siguienteTurno()}") 
print(f"Turno de: {j.siguienteTurno()}") 

print("\n--- Eliminando a Ana ---")
j.eliminarJugador("Ana")
print(f"Turno de: {j.siguienteTurno()}") 

print(f"\n¿Hay ganador?: {j.hayGanador()}") 

print("\n--- Eliminando a Diego ---")
j.eliminarJugador("Diego")

print(f"¿Hay ganador?: {j.hayGanador()}")

if j.hayGanador():
    print(f"¡El ganador es: {j.ganador()}!")