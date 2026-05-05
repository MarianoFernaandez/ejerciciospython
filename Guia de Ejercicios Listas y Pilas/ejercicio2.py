"""

Cola de impresion con prioridad

Una impresora recibe trabajos de distintos usuarios. Los documentos marcados como "urgente" deben
insertarse al inicio de la cola; los normales al final. La impresora procesa siempre el primero de la lista.
Requerimientos:
• Modelar cada trabajo con: usuario, documento y urgente (bool).
• Implementar agregar_trabajo(usuario, doc, urgente): inserta según prioridad.
• Implementar imprimir_siguiente(): elimina y retorna el primer trabajo.
• Implementar mostrar_cola(): lista los trabajos en orden de impresión.
• Analizar: ¿qué pasa si hay varios urgentes? ¿Se respeta el orden de llegada entre ellos?

"""

#Código base:

class TrabajoImpresion:
    def __init__(self, usuario, doc, urgente=False):
        self.usuario = usuario
        self.doc = doc
        self.urgente = urgente
        self.siguiente = None

class ColaImpresion:
    def agregar_trabajo(self, usuario, doc, urgente=False): ...
    def imprimir_siguiente(self): ...
    def mostrar_cola(self): ...