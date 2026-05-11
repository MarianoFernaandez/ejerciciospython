# ---------------------------------------------------------------------------
# EJERCICIO 02: Evaluador de expresiones matemáticas
# [AUTOR: TÚ]
# ENUNCIADO: Shunting-Yard para pasar infija a postfija y luego evaluar.
# ---------------------------------------------------------------------------
class PilaExpr:
    def __init__(self): self.elementos = []
    def push(self, dato): self.elementos.append(dato)
    def pop(self): return self.elementos.pop() if not self.esta_vacia() else None
    def peek(self): return self.elementos[-1] if not self.esta_vacia() else None
    def esta_vacia(self): return len(self.elementos) == 0

def infija_postfija(expr):
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()
    pila = PilaExpr()
    salida = []
    precedencia = {"+":1, "-":1, "*":2, "/":2}
    
    for token in tokens:
        if token.isnumeric():
            salida.append(token)
        elif token in precedencia:
            while not pila.esta_vacia() and pila.peek() != "(" and precedencia.get(pila.peek(), 0) >= precedencia[token]:
                salida.append(pila.pop())
            pila.push(token)
        elif token == "(":
            pila.push(token)
        elif token == ")":
            while not pila.esta_vacia() and pila.peek() != "(":
                salida.append(pila.pop())
            pila.pop()
            
    while not pila.esta_vacia():
        salida.append(pila.pop())
    return " ".join(salida)

def evaluar_postfija(expr):
    tokens = expr.split()
    pila = PilaExpr()
    for token in tokens:
        if token.isnumeric():
            pila.push(int(token))
        else:
            n2 = pila.pop()
            n1 = pila.pop()
            if token == "+": pila.push(n1 + n2)
            elif token == "-": pila.push(n1 - n2)
            elif token == "/": pila.push(n1 / n2)
            elif token == "*": pila.push(n1 * n2)
    return pila.pop()

def calcular(expr):
    return evaluar_postfija(infija_postfija(expr))

# --------------------------------------------------------------------------------

print("--- Inicializando Evaluador de Expresiones ---")

# 1. Expresión sin paréntesis (la multiplicación tiene prioridad)
expresion1 = "3 + 4 * 2"
print(f"\n1. Evaluando: {expresion1}")
print(f"   -> Transformación Postfija: {infija_postfija(expresion1)}")
print(f"   -> Resultado final: {calcular(expresion1)} (Esperado: 11)")

# 2. Expresión con paréntesis (forzamos la suma primero)
expresion2 = "( 3 + 4 ) * 2"
print(f"\n2. Evaluando: {expresion2}")
print(f"   -> Transformación Postfija: {infija_postfija(expresion2)}")
print(f"   -> Resultado final: {calcular(expresion2)} (Esperado: 14)")

# 3. Expresión combinada con división
expresion3 = "10 / 2 + 3"
print(f"\n3. Evaluando: {expresion3}")
print(f"   -> Transformación Postfija: {infija_postfija(expresion3)}")
print(f"   -> Resultado final: {calcular(expresion3)} (Esperado: 8.0)")