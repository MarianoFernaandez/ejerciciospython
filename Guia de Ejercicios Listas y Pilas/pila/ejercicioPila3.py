# ---------------------------------------------------------------------------
# EJERCICIO 03: Simulación de call stack
# [AUTOR: ]
# ENUNCIADO: Simula el call stack lanzando error si supera cierta profundidad.
# ---------------------------------------------------------------------------
class CallStack:
    def __init__(self, limite=10):
        self.stack = []
        self.limite = limite

    def llamar(self, funcion, params, linea):
        if len(self.stack) >= self.limite:
            raise RecursionError("Maximum call stack size exceeded")
        frame = {"funcion": funcion, "params": params, "linea": linea}
        self.stack.append(frame)

    def retornar(self):
        if self.stack:
            return self.stack.pop()
        return None

    def mostrar_stack(self):
        for i, frame in enumerate(reversed(self.stack)):
            print(f"Tope {i}: {frame['funcion']} | Params: {frame['params']} | Lín: {frame['linea']}")

# -----------------------------------------------------------------------------------------------------

print("--- Inicializando Simulación de Call Stack (Límite: 5) ---")
# Le ponemos un límite pequeño (5) para poder probar el desbordamiento fácilmente
cs = CallStack(limite=5)

print("\n--- Simulando llamadas recursivas a factorial(4) ---")
try:
    # Simulamos que la función factorial se llama a sí misma reduciendo 'n'
    cs.llamar("factorial", {"n": 4}, linea=10)
    cs.llamar("factorial", {"n": 3}, linea=12)
    cs.llamar("factorial", {"n": 2}, linea=12)
    cs.llamar("factorial", {"n": 1}, linea=12)
    
    print("\nEstado del Call Stack (Tope 0 es la función ejecutándose ahora mismo):")
    cs.mostrar_stack()
    
    print("\n--- Las funciones empiezan a retornar (Resolviendo el factorial) ---")
    print(f"Retorna y sale: {cs.retornar()}") # Retorna factorial(1)
    print(f"Retorna y sale: {cs.retornar()}") # Retorna factorial(2)
    
    print("\nEstado del Call Stack tras finalizar las dos últimas llamadas:")
    cs.mostrar_stack()
    
    print("\n--- Forzando un Stack Overflow (RecursionError) ---")
    print("Vamos a llenar la pila a propósito...")
    cs.llamar("otra_funcion", {"x": 1}, linea=20)
    cs.llamar("otra_funcion", {"x": 2}, linea=21)
    cs.llamar("otra_funcion", {"x": 3}, linea=22)
    
    # Esta última llamada superará el límite de 5
    cs.llamar("funcion_fatal", {}, linea=99) 

except RecursionError as e:
    print(f"¡Error capturado con éxito!: {e}")