"""

Historial de navegación

Un navegador guarda las páginas visitadas. Cada vez que el usuario visita una URL nueva, se agrega al
frente de la lista. El botón "atrás" muestra el historial en orden cronológico inverso.
Requerimientos: 
• Modelar el historial como lista simple donde la cabeza es la página actual.
• Implementar visitar(url): inserta al inicio.
• Implementar mostrar_historial(n=10): imprime las últimas N páginas visitadas.
• Implementar la lógica para evitar duplicados: si la URL ya existe en la lista, no la agrega de nuevo sino que la mueve al frente.

"""

#Codigo Base

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Historial:
    def __init__(self):
        self.cabeza = None

    def visitar(self, url):
        actual = self.cabeza
        anterior = None

        if self.cabeza is None:
            self.cabeza = Nodo(url)
            return
        
        while actual is not None:
            if actual.dato == url:
                break

            anterior = actual
            actual = actual.siguiente

        if actual is not None:
            if anterior is not None:
                anterior.siguiente = actual.siguiente
            else:
                return
        else:
            actual = Nodo(url)
            
        actual.siguiente = self.cabeza
        
        self.cabeza = actual


    def mostrar_historial(self, n=10): 

        actual = self.cabeza
        contador = 0

        print("Estado actual del historial:")

        while actual is not None and contador < n:

            print(f"-->{actual.dato}")

            actual = actual.siguiente

            contador += 1

# -----------------------------------------------------------------------------------------------

# Uso esperado:
miHistorial = Historial()
miHistorial.visitar("python.org")
miHistorial.visitar("reactnative.dev")
miHistorial.visitar("education.minecraft.net")
miHistorial.visitar("fastapi.tiangolo.com")
miHistorial.visitar("bocajuniors.com.ar")
miHistorial.visitar("en.psg.fr")
miHistorial.visitar("mysql.com")
miHistorial.visitar("expo.dev")
miHistorial.visitar("examine.com/supplements/creatine/")
miHistorial.visitar("learn.microsoft.com/en-us/dotnet/csharp/")
miHistorial.visitar("flask.palletsprojects.com")
miHistorial.visitar("pcpartpicker.com")
miHistorial.visitar("developer.mozilla.org")
miHistorial.visitar("microsoft.com/sql-server")
miHistorial.visitar("github.com") 

miHistorial.visitar("bocajuniors.com.ar") # mueve al frente, no duplica

miHistorial.mostrar_historial()
# → google.com → github.com