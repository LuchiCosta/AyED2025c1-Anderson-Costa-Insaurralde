from modules.vertice import Vertice

class Grafo:
    def __init__(self):
        # Constructor del objeto Grafo.
        self.listaVertices = {} #diccionario de vertices
        self.numVertices = 0

    def agregarVertice(self, nombre):
        nombre = nombre.strip()
        # Agrega un vértice al grafo.
        if nombre not in self.listaVertices: #si el vertice no existe
            self.numVertices += 1 #incremento el numero de vertices
            nuevoVertice = Vertice(nombre) #creo un nuevo vertice
            self.listaVertices[nombre] = nuevoVertice #lo agrego al diccionario
            return nuevoVertice
        return self.listaVertices[nombre] #si ya existe, lo devuelvo

    def obtenerVertice(self, nombre):
        nombre = nombre.strip()
        # Devuelve un vértice del grafo.
        if nombre in self.listaVertices: #si el vertice existe
            return self.listaVertices[nombre] #devuelvo el vertice del diccionario
        else:
            return None

    def __contains__(self, nombre):
        nombre = nombre.strip()
        # Verifica si un vértice está en el grafo.
        return nombre in self.listaVertices
        #devuelve true si el vertice existe con ese nombre, false si no

    def agregarArista(self, de, a, distancia=0):
        de = de.strip()
        a = a.strip()
        # Agrega una arista entre dos vértices (de y a).
        if de not in self.listaVertices: #si no estan, los agrego
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], distancia)
        #agrego el vecino al vertice de origen con la distancia

    def obtenerVertices(self):
        # Devuelve una lista de los nombres de los vértices del grafo.
        return list(self.listaVertices.keys()) 
        # keys devuelve los nombres de los vertices

    def __iter__(self):
        # Permite iterar sobre los vértices del grafo.
        return iter(self.listaVertices.values())
        #values son los objetos Vertice del grafo
    
    def recorrer(self, destino):
        # Método para recorrer el grafo desde un vértice destino.
        recorrido = []
        while destino: # inicio con el destino (final de la ruta)
            recorrido.append(destino.obtenerId()) #guardo el nombre del vertice
            if destino.obtenerPredecesor() is not None:
                #si tiene predecesor, lo agrego al recorrido y obtengo su ponderación
                recorrido.append(destino.obtenerPredecesor().obtenerPonderacion(destino))
            destino = destino.obtenerPredecesor() #actualizo destino al predecesor
        recorrido.reverse() #para mostrarlo desde el inicio al final
        cadena = recorrido[0]
        for i in range(1, len(recorrido)):
            #armo la cadena con los nombres de los vertices y las ponderaciones
            cadena += '---'
            if type(recorrido[i]) == int:
                cadena += '(' + str(recorrido[i]) + ')'
            else:
                cadena += str(recorrido[i])
        return cadena

if __name__ == "__main__":
    g = Grafo()
    g.agregarVertice("a")
    g.agregarVertice("b")
    g.agregarVertice("c")   
    g.agregarVertice("d")

    g.listaVertices
    
    g.agregarArista("a","b",5)
    g.agregarArista("c","d",2)
    g.agregarArista("a","c",4)
    g.agregarArista("b","d",9)
    
    print(g.obtenerVertices())
    print(g.obtenerVertice("a"))
    
    for v in g:
        for w in v.obtenerConexiones():
            print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))

