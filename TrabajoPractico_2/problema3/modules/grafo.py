from modules.vertice import Vertice

class Grafo:
    def __init__(self):
        # Constructor del objeto Grafo.
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, nombre):
        nombre = nombre.strip()
        # Agrega un vértice al grafo.
        if nombre not in self.listaVertices:
            self.numVertices += 1
            nuevoVertice = Vertice(nombre)
            self.listaVertices[nombre] = nuevoVertice
            return nuevoVertice
        return self.listaVertices[nombre]

    def obtenerVertice(self, nombre):
        nombre = nombre.strip()
        # Devuelve un vértice del grafo.
        if nombre in self.listaVertices:
            return self.listaVertices[nombre]
        else:
            return None

    def __contains__(self, nombre):
        nombre = nombre.strip()
        # Verifica si un vértice está en el grafo.
        return nombre in self.listaVertices

    def agregarArista(self, de, a, distancia=0):
        de = de.strip()
        a = a.strip()
        # Agrega una arista entre dos vértices.
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], distancia)

    def obtenerVertices(self):
        # Devuelve una lista de los nombres de los vértices del grafo.
        return list(self.listaVertices.keys())

    def __iter__(self):
        # Permite iterar sobre los vértices del grafo.
        return iter(self.listaVertices.values())
    
    def recorrer(self, destino):
        # Método para recorrer el grafo desde un vértice destino.
        recorrido = []
        while destino:
            recorrido.append(destino.obtenerId())
            if destino.obtenerPredecesor() is not None:
                recorrido.append(destino.obtenerPredecesor().obtenerPonderacion(destino))
            destino = destino.obtenerPredecesor()
        recorrido.reverse()
        cadena = recorrido[0]
        for i in range(1, len(recorrido)):
            cadena += '---'
            if type(recorrido[i]) == int:
                cadena += '(' + str(recorrido[i]) + ')'
            else:
                cadena += str(recorrido[i])
        return cadena

if __name__ == "__main__":
    pass