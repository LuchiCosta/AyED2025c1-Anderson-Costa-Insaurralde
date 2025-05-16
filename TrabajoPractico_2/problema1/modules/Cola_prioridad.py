class ColaPrioridad:
    """
    Clase ColaPrioridad
    Esta clase implementa una cola de prioridad para gestionar pacientes en una sala de emergencias.
    Los pacientes se ordenan según su nivel de criticidad, donde 1 es el más crítico y 3 es el menos crítico.
    """

    def __init__(self):
        """
        Inicializa la cola de prioridad vacía.
        """
        self.cola_prioridad = [0]
        self.tamanio = 0

    def infiltrar_arriba(self, i):
        """
        Infiltra un paciente en la cola de prioridad hacia arriba según su nivel de criticidad.
        
        :param i: Índice del paciente a infiltrar.
        """
        while i // 2 > 0:
            if self.cola_prioridad[i] < self.cola_prioridad[i // 2]:
                tmp = self.cola_prioridad[i // 2]
                self.cola_prioridad[i // 2] = self.cola_prioridad[i]
                self.cola_prioridad[i] = tmp
            i = i // 2

    def agregar_paciente(self, paciente):
        """
        Agrega un paciente a la cola de prioridad.
        
        :param paciente: Objeto Paciente a agregar a la cola.
        """
        self.cola_prioridad.append(paciente)
        self.tamanio += 1
        self.infiltrar_arriba(self.tamanio)

    def infiltrar_abajo(self, i):
        """
        Infiltra un paciente hacia abajo en la cola de prioridad.
        
        :param i: Índice del paciente a infiltrar.
        """
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

    def eliminar_paciente(self):
        """
        Elimina el paciente con mayor criticidad de la cola de prioridad.
        """
        valor_sacado = self.cola_prioridad[1]
        self.cola_prioridad[1] = self.cola_prioridad[self.tamanio]
        self.tamanio -= 1
        self.cola_prioridad.pop()
        self.infiltrar_abajo(1)
        return valor_sacado

    def construir_cola(self, lista):
        """
        Construye la cola de prioridad a partir de una lista de pacientes.
        
        :param lista: Lista de pacientes a agregar a la cola.
        """
        i = len(lista) // 2
        self.tamanio = len(lista)
        self.cola_prioridad = [0] + lista[:]
        while i > 0:
            self.infiltrar_abajo(i)
            i -= 1

    def esta_vacia(self):
        """
        Devuelve True si la cola está vacía, False en caso contrario.
        """
        return self.tamanio == 0



class Paciente:
    def __init__(self, riesgo, llegada, nombre):
        self.riesgo = riesgo        # 1: crítico, 2: moderado, 3: bajo
        self.llegada = llegada      # número que representa el orden de llegada
        self.nombre = nombre

    def __lt__(self, otro):
        """
        Define el criterio de prioridad para el heap:
        - menor riesgo (valor más bajo) tiene mayor prioridad
        - si el riesgo es igual, se prioriza el que llegó antes
        """
        if self.riesgo != otro.riesgo:
            return self.riesgo < otro.riesgo
        else:
            return self.llegada < otro.llegada

    def __str__(self):
        return f"{self.nombre} (riesgo: {self.riesgo}, llegada: {self.llegada})"
    

if __name__ == "__main__":
    cola = ColaPrioridad()

    # Simulación del ingreso de pacientes con riesgo y orden de llegada
    cola.agregar_paciente(Paciente(2, 1, "María"))
    cola.agregar_paciente(Paciente(1, 2, "Juan"))
    cola.agregar_paciente(Paciente(3, 3, "Luis"))
    cola.agregar_paciente(Paciente(1, 4, "Ana"))

    print("Orden de atención:")
    while not cola.esta_vacia():
        paciente = cola.eliminar_paciente()
        print(paciente)

