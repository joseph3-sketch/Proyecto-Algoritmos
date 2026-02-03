
arbol_logistico = {
    "nombre": "Ecuador",
    "regiones": {
        "Costa": [],
        "Sierra": [],
        "Oriente": []
    }
}

grafo_rutas = {}

PRECIO_POR_KM = 0.5

def centro_existe(centro):
    for region in arbol_logistico["regiones"]:
        if centro in arbol_logistico["regiones"][region]:
            return True
    return False


def agregar_centro_arbol(centro):
    if centro_existe(centro):
        return
    if centro.lower() in ["guayaquil", "manta", "esmeraldas"]:
        region = "Costa"
    elif centro.lower() in ["quito", "cuenca", "ambato"]:
        region = "Sierra"
    else:
        region = "Oriente"

    arbol_logistico["regiones"][region].append(centro)

def agregar_ruta(origen, destino, distancia):
    distancia = float(distancia)
    agregar_centro_arbol(origen)
    agregar_centro_arbol(destino)
    if origen not in grafo_rutas:
        grafo_rutas[origen] = {}
    if destino not in grafo_rutas:
        grafo_rutas[destino] = {}
    grafo_rutas[origen][destino] = distancia
    grafo_rutas[destino][origen] = distancia

def dijkstra(grafo, inicio, fin):
    if inicio not in grafo or fin not in grafo:
        return float("inf")

    visitados = set()
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0

    while len(visitados) < len(grafo):
        actual = None
        menor = float("inf")

        for nodo in grafo:
            if nodo not in visitados and distancias[nodo] < menor:
                menor = distancias[nodo]
                actual = nodo

        if actual is None:
            break

        visitados.add(actual)

        for vecino, peso in grafo[actual].items():
            nueva = distancias[actual] + peso
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva

    return distancias[fin]

def calcular_costo(origen, destino):
    distancia_total = dijkstra(grafo_rutas, origen, destino)
    if distancia_total == float("inf"):
        return None
    return distancia_total * PRECIO_POR_KM
