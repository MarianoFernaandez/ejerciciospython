class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def mostrar(self):
        print(self.elementos)



def evaluar_postfija(expr):
    tokens = expr.split()
    pila = Pila()
    for token in tokens:
        if token.isnumeric():
            pila.push(int(token))
        else:
            n1 = pila.pop()
            n2 = pila.pop()
            if token == "+":
                resultado = n1 + n2
                pila.push(resultado)
            elif token == "-" : 
                resultado = n2 - n1
                pila.push(resultado) 
            elif token == "/" : 
                resultado = n2 / n1
                pila.push(resultado) 
            elif token == "*" : 
                resultado = n1 * n2
                pila.push(resultado)
        
        return pila.pop()
    
def infija_postfija(expr):
    tokens = expr.split()
    pila = Pila()
    salida = []
    precedencia = {"+":1,"-":1,"*":2,"/":2}
    for token in tokens:
        if token.isnumeric():
            salida.append(token)
        elif token in precedencia:
            while not pila.esta_vacia() and precedencia[pila.peek()] >= precedencia[token]:
                salida.append(pila.pop())
            pila.push(token)
        elif token =="(":
            pila.push(token)
            

        elif token ==")":
            while not pila.peek()=="(":
                salida.append(pila.pop())
            pila.pop()
    
    while not pila.esta_vacia():
        salida.append(pila.pop())
    return " ".join(salida)            


def calcular(expr):
    resultado = infija_postfija(expr)
    return evaluar_postfija(resultado)

calcular("3+4*2")