import sys
class Vertice:
    def __init__(self,clave):
        # Constructor del objeto Vertice.
        self.id = clave.strip()
        self.vecinos = {} #guarda los vecinos del vertice y sus distancias
        self._distancia = 0
        self.predecesor = None
        
    def obtenerDistancia(self):
        # Devuelve la distancia
        return self._distancia

    def asignarDistancia(self, valor):
        # Modifica el valor de la distancia.
        self._distancia = valor
    
    def agregarVecino(self, vecino, distancia=0):
        # Permite agregar vecinos a un vértice.
        self.vecinos[vecino] = distancia #guardo el vecino y la distancia en el diccionario

    def __str__(self):
        # Método que permite la representacion del objeto como string.
        return str(self.id) + ' Vecinos: ' + str([x.id for x in self.vecinos])

    def obtenerConexiones(self):
        # Devuelve los vecinos.
        return self.vecinos.keys() #claves del diccionario (nombres)

    def obtenerId(self):
        # Devuelve el ID del vértice.
        return self.id.strip()

    def obtenerPonderacion(self,vecino):
         # Devuelve la ponderacion respecto a un vecino.
        return self.vecinos[vecino]
    
    def asignarPredecesor(self, nuevoPred):
        #  Establece quien será el predecesor del vértice.
        self.predecesor = nuevoPred
        
    def obtenerPredecesor(self):
        # Devuelve el predecesor
        return self.predecesor
