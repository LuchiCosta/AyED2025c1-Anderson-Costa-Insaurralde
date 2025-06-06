from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6]

class Paciente:
    def __init__(self, riesgo=None, llegada=None, nombre=None):
        """
        Si no se pasan parámetros, crea un paciente aleatorio.
        Si se pasan, usa los valores dados.
        """
        if riesgo is None or llegada is None or nombre is None:
            n = len(nombres)
            self.nombre = f"{nombres[randint(0, n-1)]} {apellidos[randint(0, n-1)]}"
            self.riesgo = choices(niveles_de_riesgo, probabilidades)[0]
            self.llegada = None  # Se debe asignar llegada al agregar a la cola
        else:
            self.nombre = nombre
            self.riesgo = riesgo
            self.llegada = llegada

    def __lt__(self, otro):
        """
        Menor riesgo (valor más bajo) tiene mayor prioridad.
        Si el riesgo es igual, se prioriza el que llegó antes.
        """
        if self.riesgo != otro.riesgo:
            return self.riesgo < otro.riesgo
        else:
            # Si llegada es None, no se puede comparar, así que lo dejamos igual
            if self.llegada is None or otro.llegada is None:
                return False
            return self.llegada < otro.llegada

    def __str__(self):
        llegada_str = f", llegada: {self.llegada}" if self.llegada is not None else ""
        return f"{self.nombre} (riesgo: {self.riesgo}{llegada_str})"





