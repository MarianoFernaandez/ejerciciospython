class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = set()

    def agregar_arista(self, nodo1, nodo2):
        self.agregar_nodo(nodo1)
        self.agregar_nodo(nodo2)
        self.grafo[nodo1].add(nodo2)
        self.grafo[nodo2].add(nodo1)    

    def vecinos(self, nodo):
        return self.grafo.get(nodo, set())

    def estan_conectados(self, nodo1, nodo2):
        if nodo1 not in self.grafo or nodo2 not in self.grafo:
            return False
        if nodo1 == nodo2:
            return True
        visitados = set()
        cola = [nodo1]
        while cola:
            actual = cola.pop(0)
            if actual == nodo2:
                return True
            visitados.add(actual)
            for vecino in self.vecinos(actual):
                if vecino not in visitados:
                    cola.append(vecino)
        return False

    def el_camino_entre(self, nodo1, nodo2):
        if nodo1 not in self.grafo or nodo2 not in self.grafo:
            return False
        if nodo1 == nodo2:
            return [nodo1]

        visitados = {nodo1}
        padres = {nodo1: None}
        cola = [nodo1]

        while cola:
            actual = cola.pop(0)
            for vecino in self.vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    if vecino == nodo2:
                        camino = [nodo2]
                        while padres[camino[-1]] is not None:
                            camino.append(padres[camino[-1]])
                        return camino[::-1]
                    cola.append(vecino)
        return False
       

    def __str__(self):
        resultado = ""
        for nodo, vecinos in self.grafo.items():
            resultado += f"{nodo}: {sorted(vecinos)}\n"
        return resultado

g = Grafo()
g.agregar_nodo('A')
g.agregar_nodo('B')
g.agregar_nodo('C')
g.agregar_nodo('D')
g.agregar_nodo('E')
g.agregar_arista('A', 'B')
g.agregar_arista('B', 'C')
g.agregar_arista('B', 'D')
g.agregar_arista('A', 'E')  
print(g)
print('Estan conectado e y d?', g.estan_conectados('E', 'D'))
print('Camino entre e y d?', g.el_camino_entre('E', 'D'))