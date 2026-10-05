import heapq

class GrafoPonderado:
    def __init__(self):
        # Representación del grafo no dirigido y ponderado según la imagen:
        # A - B (10), A - C (8)
        # B - C (12), B - D (7), B - E (15)
        # C - D (13), C - E (4)
        # D - E (9), D - F (6)
        # E - F (20)
        self.grafo = {
            'A': [('B', 10), ('C', 8)],
            'B': [('A', 10), ('C', 12), ('D', 7), ('E', 15)],
            'C': [('A', 8), ('B', 12), ('D', 13), ('E', 4)],
            'D': [('B', 7), ('C', 13), ('E', 9), ('F', 6)],
            'E': [('B', 15), ('C', 4), ('D', 9), ('F', 20)],
            'F': [('D', 6), ('E', 20)]
        }

    def estan_conectados(self, origen, destino):
        """
        A) Determina si existe conexión entre origen y destino.
        Retorna: bool (True / False)
        """
        if origen == destino:
            return True
        pendientes = [origen]
        visitados = [origen]
        while pendientes:
            visitadoActual = pendientes.pop(0)
            if visitadoActual == destino:
                return True
            else:
                for vecino, peso in self.grafo.get(visitadoActual, []):
                    if vecino not in visitados:
                        visitados.append(vecino)
                        pendientes.append(vecino)
        return False


    def contar_caminos(self, origen, destino):
        """
        B) Cuenta la cantidad de caminos simples distintos entre origen y destino.
        Retorna: int
        """

        if origen == destino:
            return 1
        pendientes = [[origen]]
        caminosValidos = 0
        while pendientes:
            caminoActual = pendientes.pop(0)
            nodo = caminoActual[-1]
            if nodo == destino:
                caminosValidos += 1
            else:
                for vecino, peso in self.grafo.get(nodo, []):
                    if vecino not in caminoActual:
                        nuevoCamino = caminoActual + [vecino]
                        pendientes.append(nuevoCamino)
        return caminosValidos

    def camino_mas_barato(self, origen, destino):
        """
        C) Encuentra el camino de menor costo total (suma de pesos) usando Dijkstra.
        Retorna: tuple -> (costo_minimo, ['A', ..., 'F']) o (float('inf'), None) si no hay ruta
        """
        if origen == destino:
           return (0, [origen])
        pendientes = [(0, [origen])]
        visitados = set()
        while pendientes:
            costoActual, caminoActual = heapq.heappop(pendientes)
            nodoActual = caminoActual[-1]           
            if nodoActual == destino:
                return (costoActual, caminoActual)
            else:
                if nodoActual in visitados:
                    continue
                visitados.add(nodoActual)
                for vecino, peso in self.grafo.get(nodoActual, []):
                    if vecino not in visitados:
                        nuevoCosto = costoActual + peso
                        nuevoCamino = caminoActual + [vecino]
                        heapq.heappush(pendientes, (nuevoCosto, nuevoCamino))
        return (float('inf'), None  )

if __name__ == "__main__":
    g = GrafoPonderado()

    # Pruebas:
    # print(g.estan_conectados('A', 'F'))
    print(g.estan_conectados('A', 'F'))

    # print(g.contar_caminos('A', 'F'))
    print(g.contar_caminos('A', 'F'))
    
    # print(g.camino_mas_barato('A', 'F'))
    print(g.camino_mas_barato('A', 'F'))
