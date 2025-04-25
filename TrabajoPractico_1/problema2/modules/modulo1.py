# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class nodo: #permite recorrer la lista en ambos sentidos
    def __init__(self, dato): 
        self.dato = dato #almacena el dato
        self.anterior = None #puntero al numero anterior
        self.siguiente = None #puntero al numero siguiente

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None #aun no hay primer elemento
        self.cola = None #tampoco hay ultimo elemento aun
        self.tamanio = 0 #inicia en cero
    
    def esta_vacia(self):
        return self.primero is None #si devuelve true, esta vacia
    
    def __len__(self):
        return self._tamanio #devuelve la cantidad elementos de la lista

    def agregar_al_inicio(self, item):
        nuevo = nodo(item) #agregamos un nuevo nodo al inicio

        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        
        else: 
            nuevo.siguiente = self.cabeza #nuevo nodo apunta a la cabeza actual
            self.cabeza.anterior = nuevo #la cabeza actual apunta al nuevo nodo
            self.cabeza = nuevo #la cabeza es el nuevo nodo
        self._tamanio += 1 #aumenta el tamaño de la lista en 1 

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
            anterior = actual.anterior #guardo el nodo anterior
            anterior.siguiente = nuevo #ahora su nodo es el siguiente
            nuevo.anterior = anterior #ahora sabe quien esta antes
            nuevo.siguiente = actual #sabe cual es el siguiente
            actual.anterior = nuevo 
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lísta vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0  or posicion >= self.tamanio:
            raise IndexError("Posición inválida")
        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
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
        
        self._tamanio -= 1
        return dato
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente #copia nodo por nodo, lo agrega a una nueva lista llamada copia
        
        return copia
    
    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior #invierte el siguiente y el anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza #intercambio primero y ultimo

    def concatenar(self,otraLista):
        copia = otraLista.copiar() #creo una copia de otraLista y la almaceno en copia
        actual = copia.cabeza 
        while actual:
            self.agregar_al_final(actual.dato) #agrega cada nodo al final de la actual
            actual = actual.siguiente 
    
    def __add__(self, otraLista):
        resultado = self.copiar()
        resultado.concatenar(otraLista)
        return resultado
    



        
        




        




