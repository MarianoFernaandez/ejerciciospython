"""

Playlist de música con reproducción

Una app de música mantiene una playlist. El usuario puede avanzar canción, eliminar la canción actual o
agregar una canción "a continuación" (justo después de la que suena ahora).
Requerimientos:
• Mantener un puntero actual a la canción en reproducción.
• Implementar siguiente(): avanza al próximo nodo.
• Implementar agregar_a_continuacion(cancion): inserta justo después del nodo actual.
• Implementar eliminar_actual(): quita la canción actual y avanza al siguiente.
• Considerar el caso borde: ¿qué pasa cuando se elimina el único elemento de la playlist?

"""

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None

class Playlist:
    def __init__(self):
        self.cabeza = None
        self.reproduciendo = None

    def Agregar(self, cancion):
        nuevo = Nodo(cancion)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.reproduciendo = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente

            actual.siguiente = nuevo

   
    def cancionSiguiente(self):
        """Avanza el puntero de reproducción a la próxima canción."""

        if self.reproduciendo is None:
            print("No hay niguna cancion reproduciondose actualmente")
            return
        
        self.reproduciendo = self.reproduciendo.siguiente

        if self.reproduciendo is not None:
            print(f"Avanzando... Ahora suena {self.reproduciendo.cancion}")
        else:
            print("Se alcanzo el final de la playlist. La musica se detuvo")

   
    def agregar_a_continuacion(self, cancion):
        """Inserta una canción nueva justo después de la que suena ahora."""

        if self.reproduciendo is None:
            print("No se puede agregar: no hay ninguna canción reproduciéndose.")
            return
        
        nuevoNodo = Nodo(cancion) 
        # Cantante ---> Resto de la fila

        nuevoNodo.siguiente = self.reproduciendo.siguiente  
        # Cantante ---> Resto de la fila    #Nuevo Amigo ---> Resto de la fila

        self.reproduciendo.siguiente = nuevoNodo
        #Cantante ---> Nuevo Amigo ---> Resto de la fila

        print(f"Cancion agregada. A continucion {cancion}")

    def eliminar_actual(self):
        """Quita la canción que suena ahora y avanza a la siguiente."""
        
        if self.reproduciendo is None:
            print("La playlist esta vacia")
            return

        nodoSiguiente = self.reproduciendo.siguiente

        if self.reproduciendo ==  self.cabeza:
            self.cabeza = nodoSiguiente
        else:
            nodoAnterior = self.cabeza

            while nodoAnterior.siguiente != self.reproduciendo:
                nodoAnterior = nodoAnterior.siguiente

            nodoAnterior.siguiente = nodoSiguiente
        
        print(f"Eliminado: {self.reproduciendo.cancion}")
        self.reproduciendo = nodoSiguiente





play = Playlist()

play.Agregar("quavo")
play.Agregar("pepe")
play.Agregar("MIA")

print("--- Inicio de la prueba ---")
# 1. Empieza quavo
print(f"1. Sonando ahora: {play.reproduciendo.cancion}") 

# 2. Avanza a pepe
play.cancionSiguiente() 

# 3. Agrega redhot justo después de pepe
# Fila: quavo -> pepe -> redhot -> MIA
play.agregar_a_continuacion("redhot") 

# 4. Elimina pepe (la actual)
# El método eliminar_actual ya pone a redhot como la nueva "reproduciendo"
play.eliminar_actual() 

# VERIFICACIÓN CRÍTICA: ¿Qué está sonando justo después de borrar?
print(f"Esperado: redhot. Realidad: {play.reproduciendo.cancion}")

# 5. Ahora sí, avanzamos a la última
play.cancionSiguiente() # Debería ser MIA


                
        