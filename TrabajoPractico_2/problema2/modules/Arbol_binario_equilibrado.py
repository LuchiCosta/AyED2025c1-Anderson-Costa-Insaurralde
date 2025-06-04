from modules.nodoArbol import NodoArbol

class ArbolBinarioEquilibrado:

    def __init__(self):
        self.__raiz = None
        self.__tamano = 0
    
    @property
    def raiz(self):
         return self.__raiz
    
    @raiz.setter
    def raiz(self, nueva_raiz):
        self.__raiz = nueva_raiz
    
    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self, nuevo_tamano):
        self.__tamano = nuevo_tamano

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano
    

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
    
    def rotarDerecha(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)

    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
                else:
                    self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
                if nodo.hijoIzquierdo.factorEquilibrio < 0:
                    self.rotarIzquierda(nodo.hijoIzquierdo)
                    self.rotarDerecha(nodo)
                else:
                    self.rotarDerecha(nodo)     

    def obtener(self, clave):
        # Método público para obtener el valor de la raiz
        if self.raiz: 
            res = self._obtener(clave, self.raiz) 
            if res: 
                return res.valor 
            else: 
                return None 
        else: 
            return None 

    def _obtener(self, clave, nodoActual):
        # Método auxiliar recursivo para buscar un nodo por su clave
        if not nodoActual: 
            return None 
        elif nodoActual.clave == clave: # Si la clave del nodo actual coincide con la clave buscada
            return nodoActual 
        elif clave < nodoActual.clave: # Si la clave buscada es menor que la clave del nodo actual
            return self._obtener(clave, nodoActual.hijoIzquierdo) # Busca recursivamente en el subárbol izquierdo
        else: # Si la clave buscada es mayor que la clave del nodo actual
            return self._obtener(clave, nodoActual.hijoDerecho) # Busca recursivamente en el subárbol derecho

    def eliminar(self, clave):
        # Método público para eliminar un nodo con una clave específica
        if self.tamano > 1: # Si el árbol tiene más de un nodo
            nodoARemover = self._obtener(clave, self.raiz) # Busca el nodo a remover
            if nodoARemover: # Si el nodo fue encontrado
                self._eliminar(nodoARemover) # Llama al método auxiliar _eliminar para removerlo
                self.tamano -= 1 # Decrementa el tamaño del árbol
            else: # Si el nodo no fue encontrado
                raise KeyError("La clave no se encuentra en el árbol") # Lanza una excepción
        elif self.tamano == 1 and self.raiz.clave == clave: # Si el árbol tiene solo un nodo y es el que se quiere eliminar
            self.raiz = None # La raíz se vuelve None (árbol vacío)
            self.tamano = 0 # El tamaño se vuelve 0
        else: # Si el árbol está vacío o el nodo no se encuentra
            raise KeyError("La clave no se encuentra en el árbol") # Lanza una excepción

    def _eliminar(self, nodoActual):
        # Método auxiliar privado para eliminar un nodo específico
        if nodoActual.esHoja(): # Caso 1: El nodo a eliminar es una hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo: # Si es el hijo izquierdo de su padre
                nodoActual.padre.hijoIzquierdo = None # Desconecta el nodo del lado izquierdo del padre
            else: # Si es el hijo derecho de su padre
                nodoActual.padre.hijoDerecho = None # Desconecta el nodo del lado derecho del padre
            self.actualizarEquilibrioEliminacion(nodoActual.padre, 'hoja', nodoActual.esHijoIzquierdo()) # Actualiza el balance desde el padre

        elif nodoActual.tieneAmbosHijos(): # Caso 2: El nodo a eliminar tiene ambos hijos
            sucesor = nodoActual.encontrarSucesor() # Encuentra el sucesor (el nodo más pequeño en su subárbol derecho)
            # Primero actualizamos el balanceo del padre del sucesor antes de mover el sucesor
            self.actualizarEquilibrioEliminacion(sucesor.padre, 'sucesor', sucesor.esHijoIzquierdo())
            sucesor.empalmar() # Desconecta el sucesor de su posición originalf
            nodoActual.clave = sucesor.clave # Reemplaza la clave del nodo a eliminar con la clave del sucesor
            nodoActual.valor = sucesor.valor # Reemplaza el valor del nodo a eliminar con el valor del sucesor
        else: # Caso 3: El nodo a eliminar tiene un solo hijo (izquierdo o derecho)
            if nodoActual.tieneHijoIzquierdo(): # Si tiene hijo izquierdo
                if nodoActual.esHijoIzquierdo(): # Si el nodo actual es hijo izquierdo de su padre
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # El hijo del nodo a eliminar se conecta al padre del nodo a eliminar
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo # El padre del nodo a eliminar apunta al hijo
                elif nodoActual.esHijoDerecho(): # Si el nodo actual es hijo derecho de su padre
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # El hijo del nodo a eliminar se conecta al padre del nodo a eliminar
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo # El padre del nodo a eliminar apunta al hijo
                else: # Si el nodo actual es la raíz y tiene un hijo izquierdo
                    nodoActual.hijoIzquierdo.padre = None # El hijo izquierdo se convierte en la nueva raíz (sin padre)
                    self.raiz = nodoActual.hijoIzquierdo # Actualiza la raíz del árbol
                self.actualizarEquilibrioEliminacion(nodoActual.padre, 'un_hijo', nodoActual.esHijoIzquierdo()) # Actualiza el balance
            else: # Si tiene hijo derecho
                if nodoActual.esHijoIzquierdo(): # Si el nodo actual es hijo izquierdo de su padre
                    nodoActual.hijoDerecho.padre = nodoActual.padre # El hijo del nodo a eliminar se conecta al padre del nodo a eliminar
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho # El padre del nodo a eliminar apunta al hijo
                elif nodoActual.esHijoDerecho(): # Si el nodo actual es hijo derecho de su padre
                    nodoActual.hijoDerecho.padre = nodoActual.padre # El hijo del nodo a eliminar se conecta al padre del nodo a eliminar
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho # El padre del nodo a eliminar apunta al hijo
                else: # Si el nodo actual es la raíz y tiene un hijo derecho
                    nodoActual.hijoDerecho.padre = None # El hijo derecho se convierte en la nueva raíz (sin padre)
                    self.raiz = nodoActual.hijoDerecho # Actualiza la raíz del árbol
                self.actualizarEquilibrioEliminacion(nodoActual.padre, 'un_hijo', nodoActual.esHijoIzquierdo()) # Actualiza el balance

    def actualizarEquilibrioEliminacion(self, nodo, tipo_eliminacion, era_hijo_izquierdo):
        # Método para actualizar el factor de equilibrio después de una eliminación
        # y propagar los ajustes hacia arriba.
        if nodo is None: # Caso base: si el nodo es None, no hay nada que hacer
            return

        # Ajusta el factor de equilibrio del nodo actual basado en el tipo de eliminación y de qué lado era el hijo
        if tipo_eliminacion == 'hoja': # Si el nodo eliminado era una hoja
            if era_hijo_izquierdo: # Y era el hijo izquierdo
                nodo.factorEquilibrio -= 1 # El subárbol izquierdo del padre se acortó
            else: # Y era el hijo derecho
                nodo.factorEquilibrio += 1 # El subárbol derecho del padre se acortó
        elif tipo_eliminacion == 'un_hijo': # Si el nodo eliminado tenía un solo hijo
            if era_hijo_izquierdo: # Y era el hijo izquierdo
                nodo.factorEquilibrio -= 1 # El subárbol izquierdo del padre se acortó
            else: # Y era el hijo derecho
                nodo.factorEquilibrio += 1 # El subárbol derecho del padre se acortó
        elif tipo_eliminacion == 'sucesor': # Si la eliminación afectó a un sucesor (al moverlo)
            if era_hijo_izquierdo: # Y el sucesor era hijo izquierdo de su padre original
                nodo.factorEquilibrio -= 1 # El subárbol izquierdo de su padre original se acortó
            else: # Y el sucesor era hijo derecho de su padre original
                nodo.factorEquilibrio += 1 # El subárbol derecho de su padre original se acortó
            
        # Reequilibra si el factor de equilibrio está fuera de rango
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo) # Realiza las rotaciones necesarias
            # Después de reequilibrar, si el nodo rotado no es la raíz y su FE se volvió 0 (rotación simple)
            # no se necesita propagar más. Si su FE no es 0 (rotación doble), se propaga.
            # Aquí, la lógica simplificada asume que reequilibrar ya maneja la propagación del factor de equilibrio.
        elif nodo.factorEquilibrio == 0: # Si el factor de equilibrio del nodo se volvió 0 (después de un ajuste)
            if nodo.padre: # Y tiene padre
                # Propagamos el ajuste hacia arriba, porque el cambio de altura se propagó hasta aquí
                self.actualizarEquilibrioEliminacion(nodo.padre, tipo_eliminacion, nodo.esHijoIzquierdo())

    def __iter__(self): 
        # Iterador in-order del árbol
        def in_order(nodo):
            if nodo:
                yield from in_order(nodo.hijoIzquierdo)
                yield nodo
                yield from in_order(nodo.hijoDerecho)
        return in_order(self.raiz)
    
    def __contains__(self, clave):
        if self._obtener(clave, self.raiz):
            return True
        else:
            return False

class Iterador:
    def __init__(self, arbol, clave):
        self.raiz = arbol._obtener(clave, arbol.raiz)

    def __iter__(self):
        return self

    def __next__(self):
        salida = self.raiz
        if salida:
            self.raiz = salida.encontrarSucesor()

        if not salida:
            raise StopIteration # corta la itracion cuando salida es none

        return salida

    def __str__(self):
        return str(self.raiz)

if __name__=="__main__":
    avl = ArbolBinarioEquilibrado()
    avl.agregar("a",22)
    avl.agregar("b", 30)
    avl.agregar("c", 32)

    for nodo in avl:
        print(nodo)

    avl.eliminar("b")
    print("Despues de eliminar b")
    for nodo in avl:
        print(nodo)
