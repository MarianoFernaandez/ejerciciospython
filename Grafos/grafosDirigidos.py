class GrafoDirigido:
    def __init__(self):
        # Representación del grafo según el diagrama:
        # A -> B, C
        # B -> C
        # C -> D, E
        # D -> (ninguno)
        # E -> B
        self.grafo = {
            'A': ['B', 'C'],
            'B': ['C'],
            'C': ['D', 'E'],
            'D': [],
            'E': ['B']
        }
    def estan_conectados(self, origen, destino):
        """
        A) Determina si existe al menos un camino dirigido desde 'origen' hasta 'destino'.
        Retorna: bool (True / False)
        """
        if origen == destino:
            return True
        pendientes = [origen]
        visitados = [origen]

        while pendientes:
            nodoActual = pendientes.pop(0)
            if nodoActual == destino:
                return True
            else:
                for vecino in self.grafo.get(nodoActual, []):
                    if vecino not in visitados:
                        visitados.append(vecino)
                        pendientes.append(vecino)
        return False



    def contar_caminos(self, origen, destino):
        """
        B) Cuenta la cantidad de caminos simples distintos desde 'origen' hasta 'destino'.
        Retorna: int
        """
        if origen == destino:
            return 1
        pendientes = [[origen]]
        caminosValidos = 0
        while pendientes:
            caminoActual = pendientes.pop()
            nodoActual = caminoActual[-1]
            if nodoActual == destino:
                caminosValidos += 1
            else:
                for vecino in self.grafo.get(nodoActual, []):
                    if vecino not in caminoActual:
                        nuevoCamino = caminoActual + [vecino]
                        pendientes.append(nuevoCamino)
        return caminosValidos

    def camino_mas_corto(self, origen, destino):
        """
        C) Encuentra el camino con menor número de aristas desde 'origen' hasta 'destino'.
        Retorna: list (ejemplo: ['A', 'C', 'D']) o None si no hay conexión
        """
        if origen == destino:
            return [origen]
        else:
            pendientes = [[origen]]
            visitado = [origen]
            while pendientes:
                camino = pendientes.pop(0)
                nodoActual = camino[-1]
                if nodoActual == destino:
                    return camino
                else:
                    for vecino in self.grafo.get(nodoActual, []):
                        if vecino not in visitado:
                            visitado.append(vecino)
                            nuevoCamino = camino + [vecino]
                            pendientes.append(nuevoCamino)
            return None




# Ejemplo de uso de la plantilla:
if __name__ == "__main__":
    g = GrafoDirigido()

    # A)
    # print(g.estan_conectados('A', 'D'))
    print(g.estan_conectados("A", "D"))
    print(g.estan_conectados("B","A"))

    # B)
    # print(g.contar_caminos('A', 'D'))
    print(g.contar_caminos("B", "C"))

    # C)
    # print(g.camino_mas_corto('A', 'D'))
    print(g.camino_mas_corto("A", "D"))
    print(g.camino_mas_corto("D", "A"))