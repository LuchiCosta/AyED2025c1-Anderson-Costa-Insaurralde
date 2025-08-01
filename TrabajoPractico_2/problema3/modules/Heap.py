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
        min_elem = self.cola_prioridad[1] #encuentro el minimo elemento
        self.cola_prioridad[1] = self.cola_prioridad[self.tamanio] #reemplazo el minimo
        # con el ultimo elemento porque es mas facil para reordenar
        self.tamanio -= 1 #disminuyo el tamaño
        self.cola_prioridad.pop() #elimino el ultimo elemento que ahora es el minimo
        self._infiltrar_abajo(1) #reordeno el montículo desde la raiz porque el minimo
        # ha cambiado
        return min_elem 

    def _infiltrar_arriba(self, i):
        # Infiltra un dato hacia arriba en el montículo.
        while i // 2 > 0: #busco al padre en la posicion i // 2, si es distinto de 0 es
            #porque no estoy en la raiz
            if self.cola_prioridad[i] < self.cola_prioridad[i // 2]: # si el valor actual
                # es menor que el del padre, lo intercambio
                self.cola_prioridad[i], self.cola_prioridad[i // 2] = self.cola_prioridad[i // 2], self.cola_prioridad[i]
            i = i // 2 #actualizo i al padre, para que en el siguiente ciclo
            # se compare con el nuevo padre

    def _infiltrar_abajo(self, i):
        # Infiltra un dato hacia abajo en el montículo.
        while (i * 2) <= self.tamanio: #si tiene hijo izquierdo 
            #porque si i * 2 es mayor que el tamaño, no tiene hijos
            hm = self._hijo_min(i)# obtengo el hijo con el valor minimo para poder comparar
            if self.cola_prioridad[i] > self.cola_prioridad[hm]: #comparo el nodo actual
                # con el hijo con el valor minimo
                # si el valor del nodo actual es mayor que el del hijo, lo intercambio
                self.cola_prioridad[i], self.cola_prioridad[hm] = self.cola_prioridad[hm], self.cola_prioridad[i]
            i = hm #actualizo i al hijo con el valor minimo, para que en el siguiente ciclo
            # se compare con el nuevo hijo

    def _hijo_min(self, i):
        # Devuelve el índice del hijo con el valor mínimo.
        if i * 2 + 1 > self.tamanio: #si i * 2 + 1 es mayor que el tamaño, 
            # significa que solo tiene hijo izquierdo porque no tiene derecho
            return i * 2 #hijo izquierdo
        else:
            if self.cola_prioridad[i * 2] < self.cola_prioridad[i * 2 + 1]: 
                #comparo los hijos para ver cual es el menor
                return i * 2 #hijo izquierdo
            else:
                return i * 2 + 1 #hijo derecho

    def esta_vacio(self):
        # Verifica si el montículo está vacío.
        return self.tamanio == 0


