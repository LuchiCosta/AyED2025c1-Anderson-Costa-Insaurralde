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
        return self.cabeza is None #si devuelve true, esta vacia
    
    def __len__(self):
        return self.tamanio #devuelve la cantidad elementos de la lista

    def agregar_al_inicio(self, item):
        nuevo = nodo(item) #agregamos un nuevo nodo al inicio

        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        
        else: 
            nuevo.siguiente = self.cabeza #nuevo nodo apunta a la cabeza actual
            self.cabeza.anterior = nuevo #la cabeza actual apunta al nuevo nodo
            self.cabeza = nuevo #la cabeza es el nuevo nodo
        self.tamanio += 1 #aumenta el tamaño de la lista en 1 

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

    def extraer(self, posicion = None): #me posiciono uno antes del elemento
        if posicion is None:
            actual = self.cola
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        elif posicion == self.tamanio -1 or posicion == -1:
            actual = self.cola
            self.cola = actual.anterior
            self.cola.siguiente = None
        elif posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición inválida")
        elif posicion == 0:
            print
            actual = self.cabeza
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None
        elif self.tamanio == 1:
            actual = self.cabeza
            self.cabeza = None
            self.cola = None
        if  posicion !=None  and posicion < (self.tamanio-1) and posicion>0:
            actual = self.cabeza
            for _ in range(posicion):
                actual  = actual.siguiente
        
            actual.anterior.siguiente = actual.siguiente #recordar dibujito de la fila :)
            actual.siguiente.anterior = actual.anterior 
        
        self.tamanio -= 1
        return actual.dato
    
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
    
    def __iter__(self): #defino un metodo para iterar
        actual = self.cabeza 
        while actual:
            yield actual.dato  #el yield va viendo cada nodo
            actual = actual.siguiente #recorre desde el primer al ultimo nodo

    

    



        
        




        




