class Paciente:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.siguiente = None
        self.anterior = None

class Guardia:
    def __init__(self):
        self.cabeza = None

    def llega_paciente(self, nombre, prioridad):
        nuevo = Paciente(nombre, prioridad)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            if nuevo.prioridad < self.cabeza.prioridad:
                nuevo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo
                self.cabeza = nuevo
                return
            
            while actual.siguiente is not None and actual.siguiente.prioridad <= nuevo.prioridad:
                actual = actual.siguiente
                
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
            if nuevo.siguiente is not None:
                nuevo.siguiente.anterior = nuevo

    def atender(self):
        if self.cabeza is None: return None
        p = self.cabeza
        self.cabeza = self.cabeza.siguiente
        if self.cabeza: self.cabeza.anterior = None
        return p.nombre

    def mostrar_sala(self):
        inicio = self.cabeza
        while inicio is not None:
            print(f"Paciente: {inicio.nombre} | Prioridad: {inicio.prioridad}")
            inicio = inicio.siguiente

# -----------------------------------------------------------------------------------------

print("--- Inicializando la Guardia Médica ---")
guardia = Guardia()

# 1. Llegan pacientes con diferentes prioridades (1=Crítico, 5=Leve)
guardia.llega_paciente("Juan (Dolor de garganta)", 4)
guardia.llega_paciente("María (Accidente de tránsito)", 1)
guardia.llega_paciente("Pedro (Fiebre alta)", 3)

print("\nEstado de la sala de espera (María debe estar primera):")
guardia.mostrar_sala()

# 2. Llega otro paciente crítico
print("\n--- Llega nuevo paciente crítico ---")
guardia.llega_paciente("Lucía (Infarto)", 1)

print("\nEstado de la sala de espera (Lucía va después de María, antes que el resto):")
guardia.mostrar_sala()

# 3. El médico empieza a atender
print("\n--- El médico empieza a atender ---")
print(f"Atendiendo a: {guardia.atender()}")  # Debería ser María
print(f"Atendiendo a: {guardia.atender()}")  # Debería ser Lucía

print("\nEstado de la sala de espera tras atender a los críticos:")
guardia.mostrar_sala()