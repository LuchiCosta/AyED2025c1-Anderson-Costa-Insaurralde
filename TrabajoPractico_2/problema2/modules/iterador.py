from modules.Arbol_binario_equilibrado import ArbolBinarioEquilibrado
from modules.nodoArbol import NodoArbol

class Iterador:
    def __init__(self, arbol, clave):
        self.raiz = arbol._obtener(clave, arbol.raiz)

def __iter__(self):
    return self

def __next__(self):
    salida = self.raiz
    if salida:
        self.raiz = salida.encontrarSucesor()

    if not salida:
        raise StopIteration # corta la itracion cuando salida es none
    
    return salida

def __str__(self):
        return str(self.raiz)
