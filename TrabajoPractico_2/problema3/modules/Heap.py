class MonticuloMin:
    def __init__(self):
        # Inicializa el montículo.
        self.cola_prioridad = [0]  # Cambiado de 'heap' a 'cola_prioridad'
        self.tamanio = 0

    def insertar(self, dato):
        # Inserta un dato en el montículo.
        self.cola_prioridad.append(dato)
        self.tamanio += 1
        self._infiltrar_arriba(self.tamanio)

    def extraer_min(self):
        # Extrae el elemento de menor valor del montículo.
        if self.tamanio == 0:
            raise IndexError("Heap vacío")
        min_elem = self.cola_prioridad[1]
        self.cola_prioridad[1] = self.cola_prioridad[self.tamanio]
        self.tamanio -= 1
        self.cola_prioridad.pop()
        self._infiltrar_abajo(1)
        return min_elem

    def _infiltrar_arriba(self, i):
        # Infiltra un dato hacia arriba en el montículo.
        while i // 2 > 0:
            if self.cola_prioridad[i] < self.cola_prioridad[i // 2]:
                self.cola_prioridad[i], self.cola_prioridad[i // 2] = self.cola_prioridad[i // 2], self.cola_prioridad[i]
            i = i // 2

    def _infiltrar_abajo(self, i):
        # Infiltra un dato hacia abajo en el montículo.
        while (i * 2) <= self.tamanio:
            hm = self._hijo_min(i)
            if self.cola_prioridad[i] > self.cola_prioridad[hm]:
                self.cola_prioridad[i], self.cola_prioridad[hm] = self.cola_prioridad[hm], self.cola_prioridad[i]
            i = hm

    def _hijo_min(self, i):
        # Devuelve el índice del hijo con el valor mínimo.
        if i * 2 + 1 > self.tamanio:
            return i * 2
        else:
            if self.cola_prioridad[i * 2] < self.cola_prioridad[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def esta_vacio(self):
        # Verifica si el montículo está vacío.
        return self.tamanio == 0


