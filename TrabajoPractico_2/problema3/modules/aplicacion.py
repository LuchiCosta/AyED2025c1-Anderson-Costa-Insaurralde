from modules.grafo import Grafo
from modules.vertice import Vertice
from modules.Heap import MonticuloMin

def construir_grafo_aldeas(path_archivo): 
    g = Grafo()
    with open(path_archivo, encoding="utf-8") as f:
        #basicamente, organizo el archivo eliminando los espacios en blanco
        # y separando los datos por comas
        # cada linea tiene el formato: origen, destino, distancia
        # o solo el nombre de la aldea
        for linea in f:
            linea = linea.strip() #separa los datos por líneas
            if not linea:  # Ignora líneas vacías
                continue
            partes = [p.strip() for p in linea.split(",")]
            if len(partes) == 3:
                origen = partes[0]
                destino = partes[1]
                distancia = int(partes[2])
                g.agregarArista(origen, destino, distancia)
            elif len(partes) == 1 and partes[0]:
                g.agregarVertice(partes[0])
    return g

def aldeas_alfabetico(grafo):
    # Devuelve una lista de aldeas ordenadas alfabéticamente a partir de un grafo
    # que contiene aldeas y sus nombres
    return sorted(grafo.obtenerVertices()) 

def prim(grafo, inicio):
    # Inicializar distancias y predecesores
    for v in grafo:
        v.asignarDistancia(float('inf')) #toma la primer distancia como infinita, porque
        # no se ha recorrido el grafo
        v.asignarPredecesor(None) #se toma el predecesor como None porque no se lo conoce aun
    grafo.obtenerVertice(inicio).asignarDistancia(0) # la distancia al inicio es 0
    # porque es el punto de partida

    heap = MonticuloMin() #cola de prioridad
    for v in grafo:
        heap.insertar((v.obtenerDistancia(), v.obtenerId(), v)) #prioridad, nombre, objeto
        #vertice

    visitados = set() # Conjunto para almacenar los vértices visitados
    # que cada aldea se conecte solo una vez de la forma mas eficiente

    while not heap.esta_vacio():
        dist, nombre, actual = heap.extraer_min() #devuelve el vertice con la menor distancia
        if nombre in visitados: 
            continue  # Si ya fue visitado, saltar
        visitados.add(nombre)
        for vecino in actual.obtenerConexiones(): # obtener los vecinos del vertice actual
            peso = actual.obtenerPonderacion(vecino) # distancia entre el vertice actual
            # y el vecino
            if vecino.obtenerId() not in visitados and peso < vecino.obtenerDistancia():
                # Si el vecino no ha sido visitado y la distancia es menor a la actual
                vecino.asignarDistancia(peso) #asigno la nueva distancia
                vecino.asignarPredecesor(actual) #asigno el predecesor al vecino
                heap.insertar((peso, vecino.obtenerId(), vecino)) #actualizo el montículo

def obtener_rutas(grafo, inicio):
    # Devuelve una lista de diccionarios, cada uno con la info de una aldea
    rutas = []
    for v in grafo:
        nombre = v.obtenerId() #tiene el nombre de la aldea
        pred = v.obtenerPredecesor() #tiene el predecesor del vertice
        recibe_de = pred.obtenerId() if pred else None #asigna el predecesor si existe
        rutas.append({"nombre": nombre, "recibe_de": recibe_de, "envia_a": []})
        #agrego diccionario a la lista rutas con la info de la aldea
    nombre_a_ruta = {r["nombre"]: r for r in rutas} #otro diccionario para buscar las 
    #aldeas por nombre
    for v in grafo: 
        pred = v.obtenerPredecesor()
        if pred:
            nombre_a_ruta[pred.obtenerId()]["envia_a"].append(v.obtenerId())
            #pred tiene el nombre del predecesor, y si existe, se agrega el nombre del
            #v a la lista de aldeas que envían a v
    return rutas

def suma_distancias(grafo, inicio):
    # Calcula la suma total de las distancias desde el vértice de inicio a todos los demás vértices
    total = 0
    for v in grafo:
        if v.obtenerId() != inicio: #porque el inicio no tiene predecesor
            pred = v.obtenerPredecesor() 
            if pred: # Si tiene predecesor, se suma la distancia
                total += pred.obtenerPonderacion(v) #distancia parcial desde el nodo
                # anterior al actual
    return total

if __name__ == "__main__":
    grafo = construir_grafo_aldeas("docs/aldeas.txt")
    aldeas = aldeas_alfabetico(grafo)
    prim(grafo, "Pancrudo") #toma como incio peligros
    rutas = obtener_rutas(grafo, "Pancrudo") # inicia en peligros   
    total = suma_distancias(grafo, "Pancrudo") # inicia en peligros

    print("Aldeas en orden alfabético:")
    for aldea in aldeas:
        print(aldea)

    print("\nRutas óptimas:")
    for ruta in rutas:
        nombre = ruta["nombre"]
        recibe = ruta["recibe_de"]
        envia = ruta["envia_a"]
        print(f"{nombre}: recibe de {recibe}, envía a {', '.join(envia) if envia else 'nadie'}")

    print("\nSuma total de distancias:", total)

    