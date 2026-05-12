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
cs = CallStack(limite=5)

print("\n--- Simulando llamadas recursivas a factorial(4) ---")
try:
    cs.llamar("factorial", {"n": 4}, linea=10)
    cs.llamar("factorial", {"n": 3}, linea=12)
    cs.llamar("factorial", {"n": 2}, linea=12)
    cs.llamar("factorial", {"n": 1}, linea=12)
    
    print("\nEstado del Call Stack (Tope 0 es la función ejecutándose ahora mismo):")
    cs.mostrar_stack()
    
    print("\n--- Las funciones empiezan a retornar (Resolviendo el factorial) ---")
    print(f"Retorna y sale: {cs.retornar()}") 
    print(f"Retorna y sale: {cs.retornar()}") 
    
    print("\nEstado del Call Stack tras finalizar las dos últimas llamadas:")
    cs.mostrar_stack()
    
    print("\n--- Forzando un Stack Overflow (RecursionError) ---")
    print("Vamos a llenar la pila a propósito...")
    cs.llamar("otra_funcion", {"x": 1}, linea=20)
    cs.llamar("otra_funcion", {"x": 2}, linea=21)
    cs.llamar("otra_funcion", {"x": 3}, linea=22)
    
    cs.llamar("funcion_fatal", {}, linea=99) 

except RecursionError as e:
    print(f"¡Error capturado con éxito!: {e}")