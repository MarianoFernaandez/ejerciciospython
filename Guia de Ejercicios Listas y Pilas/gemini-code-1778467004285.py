"""
=============================================================================
GUÍA DE EJERCICIOS APLICADOS - ESTRUCTURAS DE DATOS EN PYTHON
Archivo Maestro Unificado y Ejecutable
=============================================================================
"""

# ===========================================================================
# 1. LISTAS SIMPLEMENTE ENLAZADAS
# ===========================================================================

# ---------------------------------------------------------------------------
# EJERCICIO 01: Historial de navegación
# [AUTOR: TÚ]
# ENUNCIADO: Un navegador guarda las páginas visitadas. Cada vez que el usuario 
# visita una URL nueva, se agrega al frente de la lista.
# ---------------------------------------------------------------------------
class NodoHistorial:
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
            self.cabeza = NodoHistorial(url)
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
            actual = NodoHistorial(url)
            
        actual.siguiente = self.cabeza
        self.cabeza = actual

    def mostrar_historial(self, n=10): 
        actual = self.cabeza
        contador = 0
        while actual is not None and contador < n:
            print(f"--> {actual.dato}")
            actual = actual.siguiente
            contador += 1


# ---------------------------------------------------------------------------
# EJERCICIO 02: Cola de impresión con prioridad
# [AUTOR: GEMINI]
# ENUNCIADO: Los trabajos "urgente" deben insertarse al inicio de la cola; 
# los normales al final.
# ---------------------------------------------------------------------------
class TrabajoImpresion:
    def __init__(self, usuario, doc, urgente=False):
        self.usuario = usuario
        self.doc = doc
        self.urgente = urgente
        self.siguiente = None

class ColaImpresion:
    def __init__(self):
        self.cabeza = None

    def agregar_trabajo(self, usuario, doc, urgente=False):
        nuevo = TrabajoImpresion(usuario, doc, urgente)
        if self.cabeza is None:
            self.cabeza = nuevo
            return

        if urgente:
            if not self.cabeza.urgente:
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                actual = self.cabeza
                while actual.siguiente and actual.siguiente.urgente:
                    actual = actual.siguiente
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def imprimir_siguiente(self):
        if self.cabeza is None:
            return "Cola vacía"
        trabajo = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return f"Imprimiendo: {trabajo.doc} de {trabajo.usuario}"

    def mostrar_cola(self):
        actual = self.cabeza
        while actual:
            tipo = "URGENTE" if actual.urgente else "Normal"
            print(f"[{tipo}] {actual.doc} ({actual.usuario})")
            actual = actual.siguiente


# ---------------------------------------------------------------------------
# EJERCICIO 03: Playlist de música con reproducción
# [AUTOR: TÚ]
# ENUNCIADO: El usuario puede avanzar, eliminar la actual o agregar a continuación.
# ---------------------------------------------------------------------------
class NodoPlaylist:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None

class Playlist:
    def __init__(self):
        self.cabeza = None
        self.reproduciendo = None

    def Agregar(self, cancion):
        nuevo = NodoPlaylist(cancion)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.reproduciendo = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def cancionSiguiente(self):
        if self.reproduciendo is None: return
        self.reproduciendo = self.reproduciendo.siguiente

    def agregar_a_continuacion(self, cancion):
        if self.reproduciendo is None: return
        nuevoNodo = NodoPlaylist(cancion) 
        nuevoNodo.siguiente = self.reproduciendo.siguiente  
        self.reproduciendo.siguiente = nuevoNodo

    def eliminar_actual(self):
        if self.reproduciendo is None: return
        nodoSiguiente = self.reproduciendo.siguiente
        if self.reproduciendo == self.cabeza:
            self.cabeza = nodoSiguiente
        else:
            nodoAnterior = self.cabeza
            while nodoAnterior.siguiente != self.reproduciendo:
                nodoAnterior = nodoAnterior.siguiente
            nodoAnterior.siguiente = nodoSiguiente
        self.reproduciendo = nodoSiguiente


# ===========================================================================
# 2. LISTAS DOBLEMENTE ENLAZADAS
# ===========================================================================

# ---------------------------------------------------------------------------
# EJERCICIO 01: Editor de texto con cursor
# [AUTOR: GEMINI]
# ENUNCIADO: El cursor puede moverse arriba/abajo, insertar línea y eliminar actual.
# ---------------------------------------------------------------------------
class NodoLinea:
    def __init__(self, texto):
        self.texto = texto
        self.siguiente = None
        self.anterior = None

class EditorTexto:
    def __init__(self):
        self.cabeza = None
        self.cursor = None 

    def insertar_linea(self, texto):
        nuevo = NodoLinea(texto)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cursor = nuevo
        else:
            nuevo.siguiente = self.cursor.siguiente
            nuevo.anterior = self.cursor
            if self.cursor.siguiente:
                self.cursor.siguiente.anterior = nuevo
            self.cursor.siguiente = nuevo
            self.cursor = nuevo

    def eliminar_linea(self):
        if self.cursor is None: return
        anterior = self.cursor.anterior
        siguiente = self.cursor.siguiente

        if anterior: anterior.siguiente = siguiente
        else: self.cabeza = siguiente
            
        if siguiente: siguiente.anterior = anterior
        self.cursor = anterior if anterior else siguiente

    def cursor_arriba(self):
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior

    def cursor_abajo(self):
        if self.cursor and self.cursor.siguiente:
            self.cursor = self.cursor.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            marca = "->" if actual == self.cursor else "  "
            print(f"{marca} {actual.texto}")
            actual = actual.siguiente


# ---------------------------------------------------------------------------
# EJERCICIO 02: Sistema undo/redo
# [AUTOR: GEMINI]
# ENUNCIADO: Undo retrocede, redo avanza. Nueva acción borra el futuro.
# ---------------------------------------------------------------------------
class NodoAccion:
    def __init__(self, accion):
        self.accion = accion
        self.siguiente = None
        self.anterior = None

class UndoRedo:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def ejecutar(self, accion):
        nuevo = NodoAccion(accion)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.actual = nuevo
        else:
            self.actual.siguiente = nuevo
            nuevo.anterior = self.actual
            self.actual = nuevo

    def undo(self):
        if self.actual and self.actual.anterior:
            accion_deshecha = self.actual.accion
            self.actual = self.actual.anterior
            return accion_deshecha
        return None

    def redo(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.accion
        return None

    def historial(self):
        nodo = self.cabeza
        while nodo:
            marca = "[ACTUAL]" if nodo == self.actual else ""
            print(f"{nodo.accion} {marca}")
            nodo = nodo.siguiente


# ---------------------------------------------------------------------------
# EJERCICIO 03: Gestión de pacientes en guardia
# [AUTOR: TÚ]
# ENUNCIADO: Guardia atiende pacientes según gravedad (1 = crítico, 5 = leve).
# ---------------------------------------------------------------------------
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


# ===========================================================================
# 3. LISTAS CIRCULARES
# ===========================================================================

# ---------------------------------------------------------------------------
# EJERCICIO 01: Turno rotativo entre jugadores
# [AUTOR: GEMINI]
# ENUNCIADO: En un juego de mesa, los jugadores se turnan en ronda.
# ---------------------------------------------------------------------------
class NodoJugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class Juego:
    def __init__(self):
        self.cabeza = None
        self.turno_actual = None

    def agregar_jugador(self, nombre):
        nuevo = NodoJugador(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
            self.turno_actual = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def siguiente_turno(self):
        if not self.turno_actual: return None
        jugador = self.turno_actual.nombre
        self.turno_actual = self.turno_actual.siguiente
        return jugador

    def eliminar_jugador(self, nombre):
        if not self.cabeza: return
        actual = self.cabeza
        anterior = None
        while True:
            if actual.nombre == nombre:
                if actual.siguiente == actual: 
                    self.cabeza = None
                    self.turno_actual = None
                    return
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    ultimo = self.cabeza
                    while ultimo.siguiente != self.cabeza:
                        ultimo = ultimo.siguiente
                    self.cabeza = actual.siguiente
                    ultimo.siguiente = self.cabeza
                
                if self.turno_actual == actual:
                    self.turno_actual = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza: break

    def ganador(self):
        return self.cabeza.nombre if self.cabeza and self.cabeza.siguiente == self.cabeza else None


# ---------------------------------------------------------------------------
# EJERCICIO 02: Problema de Josephus
# [AUTOR: TÚ]
# ENUNCIADO: N personas en círculo. Se cuenta hasta K y se elimina.
# ---------------------------------------------------------------------------
class Persona:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircularJosephus:
    def __init__(self):
        self.cabeza = None
    
    def agregar_persona(self, dato):
        p = Persona(dato)
        if not self.cabeza:
            self.cabeza = p
            p.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = p
            p.siguiente = self.cabeza

def josephus(n, k):
    l = ListaCircularJosephus()
    for i in range(1, n+1):
        l.agregar_persona(i)
    
    actual = l.cabeza
    anterior = None
    
    while actual.siguiente != actual:
        for _ in range(k-1):
            anterior = actual
            actual = actual.siguiente
        
        anterior.siguiente = actual.siguiente
        actual = actual.siguiente
        
    return actual.dato


# ---------------------------------------------------------------------------
# EJERCICIO 03: Buffer circular de logs del sistema
# [AUTOR: GEMINI]
# ENUNCIADO: Guarda N mensajes de log sobrescribiendo los antiguos.
# ---------------------------------------------------------------------------
class NodoLog:
    def __init__(self):
        self.mensaje = None
        self.siguiente = None

class RingBuffer:
    def __init__(self, capacidad):
        self.cabeza = NodoLog()
        actual = self.cabeza
        for _ in range(capacidad - 1):
            nuevo = NodoLog()
            actual.siguiente = nuevo
            actual = nuevo
        actual.siguiente = self.cabeza
        self.puntero_escritura = self.cabeza

    def registrar(self, mensaje):
        self.puntero_escritura.mensaje = mensaje
        self.puntero_escritura = self.puntero_escritura.siguiente

    def mostrar_logs(self):
        actual = self.puntero_escritura
        while True:
            if actual.mensaje is not None:
                print(actual.mensaje)
            actual = actual.siguiente
            if actual == self.puntero_escritura:
                break


# ===========================================================================
# 4. PILAS (STACKS)
# ===========================================================================

# ---------------------------------------------------------------------------
# EJERCICIO 01: Navegador web: atrás y adelante
# [AUTOR: GEMINI]
# ENUNCIADO: Usa dos pilas. Al visitar página nueva la pila adelante se vacía.
# ---------------------------------------------------------------------------
class PilaNavegador:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if not self.esta_vacia() else None
    def peek(self): return self.items[-1] if not self.esta_vacia() else None
    def esta_vacia(self): return len(self.items) == 0
    def vaciar(self): self.items = []

class NavegadorPilas:
    def __init__(self):
        self.atras_pila = PilaNavegador()
        self.adelante_pila = PilaNavegador()

    def visitar(self, url):
        self.atras_pila.push(url)
        self.adelante_pila.vaciar()

    def atras(self):
        if not self.atras_pila.esta_vacia():
            actual = self.atras_pila.pop()
            self.adelante_pila.push(actual)
            return self.atras_pila.peek()
        return None

    def adelante(self):
        if not self.adelante_pila.esta_vacia():
            siguiente = self.adelante_pila.pop()
            self.atras_pila.push(siguiente)
            return siguiente
        return None


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


# ---------------------------------------------------------------------------
# EJERCICIO 03: Simulación de call stack
# [AUTOR: GEMINI]
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


# ===========================================================================
# BLOQUE DE EJECUCIÓN - PRUEBAS AUTOMATIZADAS
# ===========================================================================
if __name__ == "__main__":
    print("========================================")
    print(" INICIANDO PRUEBAS DE ESTRUCTURAS...")
    print("========================================")

    # --- 1. LISTAS SIMPLES ---
    print("\n[LS - Ej1] Historial:")
    h = Historial()
    h.visitar("google.com")
    h.visitar("github.com")
    h.visitar("google.com") # Se mueve al frente
    h.mostrar_historial()

    print("\n[LS - Ej2] Cola Impresión:")
    cola = ColaImpresion()
    cola.agregar_trabajo("User1", "DocA.pdf")
    cola.agregar_trabajo("User2", "DocUrgente.pdf", urgente=True)
    cola.mostrar_cola()

    print("\n[LS - Ej3] Playlist:")
    play = Playlist()
    play.Agregar("quavo")
    play.Agregar("pepe")
    play.agregar_a_continuacion("redhot")
    print(f"Agregada con éxito, reproduciendo: {play.reproduciendo.cancion}")

    # --- 2. LISTAS DOBLES ---
    print("\n[LDE - Ej1] Editor Texto:")
    editor = EditorTexto()
    editor.insertar_linea("Primera linea")
    editor.insertar_linea("Segunda linea")
    editor.mostrar()

    print("\n[LDE - Ej2] Undo/Redo:")
    ur = UndoRedo()
    ur.ejecutar("escribir 'Hola'")
    ur.ejecutar("negrita")
    ur.undo()
    ur.historial()

    print("\n[LDE - Ej3] Guardia:")
    g = Guardia()
    g.llega_paciente("Ana (Leve)", 5)
    g.llega_paciente("Luis (Critico)", 1)
    g.mostrar_sala()

    # --- 3. LISTAS CIRCULARES ---
    print("\n[LC - Ej1] Juego de Mesa:")
    juego = Juego()
    for nombre in ["Ana", "Beto", "Carla"]: juego.agregar_jugador(nombre)
    juego.eliminar_jugador("Beto")
    print(f"Quedan jugando. Siguiente turno: {juego.siguiente_turno()}")

    print("\n[LC - Ej2] Josephus:")
    sobreviviente = josephus(7, 3)
    print(f"Sobreviviente de josephus(7,3): {sobreviviente}")

    print("\n[LC - Ej3] Ring Buffer Logs:")
    rb = RingBuffer(3)
    rb.registrar("Log 1")
    rb.registrar("Log 2")
    rb.registrar("Log 3")
    rb.registrar("Log 4 (Sobrescribe)")
    rb.mostrar_logs()

    # --- 4. PILAS ---
    print("\n[Pilas - Ej1] Navegador:")
    nav = NavegadorPilas()
    nav.visitar("home.com")
    nav.visitar("noticias.com")
    nav.atras()
    print(f"Pagina actual tras 'atrás': {nav.pagina_actual()}")

    print("\n[Pilas - Ej2] Shunting-Yard Expr:")
    res = calcular("3 + 4 * 2")
    print(f"Resultado de '3 + 4 * 2': {res}")

    print("\n[Pilas - Ej3] Call Stack:")
    cs = CallStack()
    cs.llamar("factorial", {"n": 4}, 1)
    cs.llamar("factorial", {"n": 3}, 1)
    cs.mostrar_stack()

    print("\n========================================")
    print(" PRUEBAS FINALIZADAS CON ÉXITO")
    print("========================================")