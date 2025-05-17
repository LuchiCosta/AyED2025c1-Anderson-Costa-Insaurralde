class nodo:
    def __init__(self, dato): 
        self.dato = dato
        self.anterior = None
        self.siguiente = None

    def __str__(self):
        return str(self.dato)


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.cabeza is None
    
    def __len__(self):
        return self.tamanio

    def agregar_al_inicio(self, item):
        nuevo = nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo = nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.tamanio += 1

    def insertar(self, item, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición inválida")
        if posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion == self.tamanio:
            self.agregar_al_final(item)
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo = nodo(item)
            anterior = actual.anterior
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.tamanio == 0:
            raise IndexError("La lista está vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0:
            posicion += self.tamanio
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición inválida")

        if self.tamanio == 1:
            actual = self.cabeza
            self.cabeza = self.cola = None
            self.tamanio -= 1
            return actual.dato
        if posicion == 0:
            actual = self.cabeza
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
            self.tamanio -= 1
            return actual.dato
        if posicion == self.tamanio - 1:
            actual = self.cola
            self.cola = actual.anterior
            self.cola.siguiente = None
            self.tamanio -= 1
            return actual.dato

        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return actual.dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otraLista):
        copia = otraLista.copiar()
        actual = copia.cabeza
        while actual:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente

    def __add__(self, otraLista):
        resultado = self.copiar()
        resultado.concatenar(otraLista)
        return resultado

    def __iter__(self):
        self._iterador = self.cabeza
        return self

    def __next__(self):
        if self._iterador is None:
            raise StopIteration
        dato = self._iterador.dato
        self._iterador = self._iterador.siguiente
        return dato
