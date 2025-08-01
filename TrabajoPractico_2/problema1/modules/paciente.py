from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6]

class Paciente:
    def __init__(self, riesgo=None, llegada=None, nombre=None):
        # Inicializa un paciente con un nivel de riesgo, hora de llegada y nombre.
        # Si no se proporcionan, se generan aleatoriamente.
        if riesgo is None or llegada is None or nombre is None:
            n = len(nombres)
            self.nombre = f"{nombres[randint(0, n-1)]} {apellidos[randint(0, n-1)]}"
            #elijo nombre y apellido al azar
            self.riesgo = choices(niveles_de_riesgo, probabilidades)[0]
            #elijo riesgo al azar
            self.llegada = None  # No se asigna hora de llegada al crear el paciente
        else:
            self.nombre = nombre
            self.riesgo = riesgo
            self.llegada = llegada

    def __lt__(self, otro): #less than
        # Compara dos pacientes primero por riesgo y luego por hora de llegada.
        if self.riesgo != otro.riesgo: # riesgo mas bajo tiene mayor prioridad
            return self.riesgo < otro.riesgo
        else:
            if self.llegada is None or otro.llegada is None:
                # si el riesgo es el mismo, comparo por hora de llegada
                return False
            return self.llegada < otro.llegada

    def __str__(self):
        # permite imprimir el paciente de forma legible.
        llegada_str = f", llegada: {self.llegada}" if self.llegada is not None else ""
        return f"{self.nombre} (riesgo: {self.riesgo}{llegada_str})"





