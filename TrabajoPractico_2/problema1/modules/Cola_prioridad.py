class ColaPrioridad:
    def __init__(self):
        # Inicializa la cola de prioridad.
        self.cola_prioridad = [0]
        self.tamanio = 0

    def infiltrar_arriba(self, i):
        # Infiltra un dato hacia arriba en la cola de prioridad.
        while i // 2 > 0:
            if self.cola_prioridad[i] < self.cola_prioridad[i // 2]:
                tmp = self.cola_prioridad[i // 2]
                self.cola_prioridad[i // 2] = self.cola_prioridad[i]
                self.cola_prioridad[i] = tmp
            i = i // 2

    def agregar(self, dato):
        # Agrega un dato a la cola de prioridad.
        self.cola_prioridad.append(dato)
        self.tamanio += 1
        self.infiltrar_arriba(self.tamanio)

    def infiltrar_abajo(self, i):
        # Infiltra un dato hacia abajo en la cola de prioridad.
        while (i * 2) <= self.tamanio:
            hm = self.hijo_min(i)
            if self.cola_prioridad[i] > self.cola_prioridad[hm]:
                tmp = self.cola_prioridad[i]
                self.cola_prioridad[i] = self.cola_prioridad[hm]
                self.cola_prioridad[hm] = tmp
            i = hm

    def hijo_min(self, i):
        if i * 2 + 1 > self.tamanio:
            return i * 2
        else:
            if self.cola_prioridad[i * 2] < self.cola_prioridad[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminar(self):
        # Elimina el elemento de mayor prioridad (el primero) de la cola.
        valor_sacado = self.cola_prioridad[1]
        self.cola_prioridad[1] = self.cola_prioridad[self.tamanio]
        self.tamanio -= 1
        self.cola_prioridad.pop()
        self.infiltrar_abajo(1)
        return valor_sacado

    def construir_cola(self, lista):
       # Construye una cola de prioridad a partir de una lista.
        i = len(lista) // 2
        self.tamanio = len(lista)
        self.cola_prioridad = [0] + lista[:]
        while i > 0:
            self.infiltrar_abajo(i)
            i -= 1

    def esta_vacia(self):
        # Verifica si la cola de prioridad está vacía.
        return self.tamanio == 0


