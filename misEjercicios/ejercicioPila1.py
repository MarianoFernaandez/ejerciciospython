"""

Un navegador usa dos pilas para gestionar la navegación: una para "atrás" y otra para "adelante". Cuando
visitás una página nueva, la pila de adelante se vacía. El botón atrás mueve la página actual a la pila de
adelante.
Requerimientos:
• Implementar visitar(url): agrega a la pila "atrás" y vacía la pila "adelante".
• Implementar atras(): mueve la página actual a "adelante" y retorna la anterior.
• Implementar adelante(): mueve de "adelante" a "atrás" y retorna esa página.
• Implementar pagina_actual(): retorna el tope de la pila "atrás".
• Manejar correctamente los casos donde no hay páginas para ir atrás o adelante.

"""

class Navegador:
    def __init__(self):
        self.pilaAtras = []
        self.pilaAdelante = []

    def paginaActual(self):
        if self.pilaAtras:
            return self.pilaAtras[-1]
        return "Navegador vacío"

    def visitar(self, url):
        self.pilaAtras.append(url)
        self.pilaAdelante = []
        print(f"Navegando a: {url}")

    def atras(self):
        if len(self.pilaAtras) > 1:
            paginaActual = self.pilaAtras.pop()
            self.pilaAdelante.append(paginaActual)
            return self.pilaAtras[-1]
        else:
            return "No hay historial para ir hacia atrás"
    
    def adelante(self):
        if len(self.pilaAdelante) > 0:
            proximaPagina = self.pilaAdelante.pop()
            self.pilaAtras.append(proximaPagina)
            return proximaPagina
        else:
            return "No hay páginas en el frente"

# ---------------------------------------------------------------------------------------------------------

nav = Navegador()
nav.visitar("google.com")
nav.visitar("youtube.com")
nav.visitar("github.com")

print(f"\n1. Página actual: {nav.paginaActual()}") 

print(f"2. Yendo atrás: {nav.atras()}")           
print(f"3. Yendo atrás: {nav.atras()}")          
print(f"4. Intento ir atrás otra vez: {nav.atras()}")

print(f"5. Yendo adelante: {nav.adelante()}")     
print(f"6. Página actual final: {nav.paginaActual()}")