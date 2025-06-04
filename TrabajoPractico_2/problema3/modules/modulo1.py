# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

from modules.grafo import Grafo

def construirGrafo(archivoPalabras):
    d = {}
    g = Grafo()
    archivo = open(archivoPalabras,'r')
    # crear baldes de palabras que se diferencian por una letra
    for linea in archivo:
        palabra = linea[:-1]
        for i in range(len(palabra)):
            balde = palabra[:i] + '_' + palabra[i+1:]
            if balde in d:
                d[balde].append(palabra)
            else:
                d[balde] = [palabra]
    # agregar vértices y aristas para palabras en el mismo balde
    for balde in d.keys():
        for palabra1 in d[balde]:
            for palabra2 in d[balde]:
                if palabra1 != palabra2:
                    g.agregarArista(palabra1,palabra2)
    return g