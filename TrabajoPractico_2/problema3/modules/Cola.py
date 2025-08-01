from modules.Heap import MonticuloMin

class ColaPrioridad:
    #la cola de prioridad es un montículo mínimo
    # que permite insertar elementos y extraer el mínimo
    # manteniendo el orden de prioridad de forma eficiente
    def __init__(self):
        self.cola_prioridad = MonticuloMin()  # Cambiado de 'monticulo' a 'cola_prioridad'

    def agregar(self, dato):
        self.cola_prioridad.insertar(dato)

    def eliminar(self):
        return self.cola_prioridad.extraer_min()

    def esta_vacia(self):
        return self.cola_prioridad.esta_vacio()

    @property
    def tamanio(self):
        return self.cola_prioridad.tamanio