class PilaExpr:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)

    def pop(self):
        return self.elementos.pop() if not self.esta_vacia() else None

    def peek(self):
        return self.elementos[-1] if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.elementos) == 0

def infija_postfija(expr):
    # Separamos todo bien para que no importe si el usuario pegó los paréntesis
    expr_limpia = expr.replace("(", " ( ").replace(")", " ) ")
    tokens = expr_limpia.split()
    
    pila = PilaExpr()
    salida = []
    precedencia = {"+": 1, "-": 1, "*": 2, "/": 2}
    
    for token in tokens:
        # Si es un número (entero o decimal), va directo a la salida
        if token.replace('.', '', 1).isdigit():
            salida.append(token)
            
        elif token == "(":
            pila.push(token)
            
        elif token == ")":
            while not pila.esta_vacia() and pila.peek() != "(":
                salida.append(pila.pop())
            pila.pop()  # Sacamos el "(" que quedó en la pila
            
        elif token in precedencia:
            while (not pila.esta_vacia() and 
                   pila.peek() != "(" and 
                   precedencia.get(pila.peek(), 0) >= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
            
    # Lo que quedó en la pila va al final
    while not pila.esta_vacia():
        salida.append(pila.pop())
        
    return " ".join(salida)

def evaluar_postfija(expr):
    tokens = expr.split()
    pila = PilaExpr()
    
    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            pila.push(float(token))
        else:
            # El orden de n2 y n1 es clave por la resta y división
            n2 = pila.pop()
            n1 = pila.pop()
            
            if token == "+":
                pila.push(n1 + n2)
            elif token == "-":
                pila.push(n1 - n2)
            elif token == "*":
                pila.push(n1 * n2)
            elif token == "/":
                if n2 != 0:
                    pila.push(n1 / n2)
                else:
                    return "Error: División por cero"
                    
    return pila.pop()

def calcular(expr):
    postfija = infija_postfija(expr)
    return evaluar_postfija(postfija)

# --------------------------------------------------------------------------------
print(f"Resultado 1: {calcular('3 + 4 * 2')}")         
print(f"Resultado 2: {calcular('(3 + 4) * 2')}")       
print(f"Resultado 3: {calcular('10 / (2 + 3)')}")      