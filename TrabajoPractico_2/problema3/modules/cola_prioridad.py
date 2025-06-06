class ColaPrioridad:
    
    def __init__(self):
        self.elementos = []

    def insertar(self, prioridad, vertice):
        self.elementos.append((prioridad, vertice))

    def extraer_min(self):
        if not self.elementos:
            return None, None
        min_idx = 0
        for i in range(1, len(self.elementos)):
            if self.elementos[i][0] < self.elementos[min_idx][0]:
                min_idx = i
        return self.elementos.pop(min_idx)

    def actualizar(self, vertice, nueva_prioridad):
        for i, (prioridad, v) in enumerate(self.elementos):
            if v == vertice:
                self.elementos[i] = (nueva_prioridad, vertice)
                break

    def contiene(self, vertice):
        return any(v == vertice for _, v in self.elementos)

    def esta_vacia(self):
        return len(self.elementos) == 0