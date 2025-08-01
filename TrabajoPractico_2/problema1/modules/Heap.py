class MonticuloMin:
    def __init__(self):
        # Inicializa el montículo.
        self.cola_prioridad = [0]  # Cambiado de 'heap' a 'cola_prioridad'
        self.tamanio = 0

    def insertar(self, dato):
        # Inserta un dato en el montículo.
        self.cola_prioridad.append(dato)
        self.tamanio += 1
        self._infiltrar_arriba(self.tamanio) #reordeno si es necesario

    def extraer_min(self):
        # Extrae el elemento de menor valor del montículo.
        if self.tamanio == 0:
            raise IndexError("Heap vacío")
        min_elem = self.cola_prioridad[1]
        self.cola_prioridad[1] = self.cola_prioridad[self.tamanio]
        #reemplazo el primer elemento por el último porque es mas facil reordenar
        self.tamanio -= 1 
        self.cola_prioridad.pop() #elimino el último elemento
        self._infiltrar_abajo(1) #reordeno desde la raiz (minimo)
        return min_elem

    def _infiltrar_arriba(self, i):
        # Infiltra un dato hacia arriba en el montículo.
        # para agregar
        while i // 2 > 0: # mientras no sea la raiz
            if self.cola_prioridad[i] < self.cola_prioridad[i // 2]:
                # Si el dato es menor que su padre, lo intercambio.
                self.cola_prioridad[i], self.cola_prioridad[i // 2] = self.cola_prioridad[i // 2], self.cola_prioridad[i]
            i = i // 2 # actualizo el índice al padre

    def _infiltrar_abajo(self, i):
        # Infiltra un dato hacia abajo en el montículo.
        #para eliminar
        while (i * 2) <= self.tamanio: # mientras tenga al menos un hijo izquierdo
            #xq se llena de izq a der
            hm = self._hijo_min(i)
            if self.cola_prioridad[i] > self.cola_prioridad[hm]:
                # si el valor del padre es mayor que el del hijo mínimo, lo intercambio.
                # por monticulo de minimos
                self.cola_prioridad[i], self.cola_prioridad[hm] = self.cola_prioridad[hm], self.cola_prioridad[i]
            i = hm # actualizo el índice al hijo mínimo

    def _hijo_min(self, i):
        # Devuelve el índice del hijo con el valor mínimo.
        if i * 2 + 1 > self.tamanio: # si esto se cumple,
            #solo tiene un hijo izquierdo porque el montículo se llena de izquierda a derecha
            return i * 2
        else:
            if self.cola_prioridad[i * 2] < self.cola_prioridad[i * 2 + 1]:
                #comparo hijo izquierdo y derecho
                return i * 2
            else:
                return i * 2 + 1

    def esta_vacio(self):
        # Verifica si el montículo está vacío.
        return self.tamanio == 0


