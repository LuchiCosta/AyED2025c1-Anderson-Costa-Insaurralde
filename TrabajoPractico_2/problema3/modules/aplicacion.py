from modules.Grafo import Grafo
from modules.vertice import Vertice
from modules.Heap import MonticuloMin

def construir_grafo_aldeas(path_archivo): 
    g = Grafo()
    with open(path_archivo, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
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
    # Devuelve una lista de aldeas ordenadas alfabéticamente
    return sorted(grafo.obtenerVertices())

def prim(grafo, inicio):
    # Inicializar distancias y predecesores
    for v in grafo:
        v.asignarDistancia(float('inf'))
        v.asignarPredecesor(None)
    grafo.obtenerVertice(inicio).asignarDistancia(0)

    heap = MonticuloMin()
    for v in grafo:
        heap.insertar((v.obtenerDistancia(), v.obtenerId(), v))

    visitados = set()

    while not heap.esta_vacio():
        dist, nombre, actual = heap.extraer_min()
        if nombre in visitados:
            continue
        visitados.add(nombre)
        for vecino in actual.obtenerConexiones():
            peso = actual.obtenerPonderacion(vecino)
            if vecino.obtenerId() not in visitados and peso < vecino.obtenerDistancia():
                vecino.asignarDistancia(peso)
                vecino.asignarPredecesor(actual)
                heap.insertar((peso, vecino.obtenerId(), vecino))

def obtener_rutas(grafo, inicio):
    # Devuelve una lista de diccionarios, cada uno con la info de una aldea
    rutas = []
    for v in grafo:
        nombre = v.obtenerId()
        pred = v.obtenerPredecesor()
        recibe_de = pred.obtenerId() if pred else None
        rutas.append({"nombre": nombre, "recibe_de": recibe_de, "envia_a": []})
    # Llenar envia_a
    nombre_a_ruta = {r["nombre"]: r for r in rutas}
    for v in grafo:
        pred = v.obtenerPredecesor()
        if pred:
            nombre_a_ruta[pred.obtenerId()]["envia_a"].append(v.obtenerId())
    return rutas

def suma_distancias(grafo, inicio):
    # Calcula la suma total de las distancias desde el vértice de inicio a todos los demás vértices
    total = 0
    for v in grafo:
        if v.obtenerId() != inicio:
            pred = v.obtenerPredecesor()
            if pred:
                total += pred.obtenerPonderacion(v)
    return total

if __name__ == "__main__":
    grafo = construir_grafo_aldeas("docs/aldeas.txt")
    aldeas = aldeas_alfabetico(grafo)
    prim(grafo, "Peligros")
    rutas = obtener_rutas(grafo, "Peligros")
    total = suma_distancias(grafo, "Peligros")

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

    # print("Aldeas detectadas:")
    # for v in grafo:
    #     print(f"'{v.obtenerId()}'")