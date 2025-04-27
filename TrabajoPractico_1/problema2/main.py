if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0  or posicion >= self.tamanio:
            raise IndexError("Posición inválida")
        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None: #me fijo que si no es None, que el anterior lo sea
                self.cabeza.anteior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        
        self.tamanio -= 1
        return dato

if posicion < -1 or posicion > self.tamanio:
            raise IndexError("Valor de posicion invalido")
        if self.tamanio == 1:
            dato = self.cabeza
            self.cabeza = None
            self.cola = None 
        elif posicion==0:
            dato = self.cabeza
            self.cabeza = dato.siguiente
            self.cabeza.anterior = None
        elif posicion == -1 or posicion == self.tamanio-1:
            dato = self.cola
            self.cola = dato.anterior
            self.cola.siguiente = None
        else:
            dato = self.cabeza
            for i in range(posicion):
                dato = dato.siguiente
                
            dato.anterior.siguiente = dato.siguiente
            dato.siguiente.anterior = dato.anterior
        self.tamanio -= 1
        return dato

anterior = actual.anterior
            siguiente = actual.siguiente
            anterior.siguiente = siguiente
            siguiente.anterior = anterior