class temperaturas_DB:
    def __init__(self, temperatura, fecha):
        self.temperatura = temperatura
        self.fecha = fecha

    def guardar_temperatura(temperatura, fecha):
        # guarda la medida de temperatura asociada a la fecha
        pass

    def devolver_temperatura(fecha):
        #devuelve la medida de temperatura en la fecha determinada
        pass

    def max_temp_rango(fecha1, fecha2):
        # devuelde la temperatura maxima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es meno a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        pass

    def min_temp_rango(fecha1, fecha2):
        # devuelde la temperatura minima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es menor a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        pass

    def temp_extremos_rango(fecha1, fecha2):
        # devuelve la temperatura minima y maxima entre los rangos fecha1 y fecha2 inclusive, fecha1 menor que fecha2
        pass

    def borrar_temperatura(fecha):
        # recibe una fecha y elimina del arbol la medicion correspondiente a esa fecha
        # borra el nodo del arbol (ver en el libro)
        pass
    
    def devolver_temperaturas(fecha1, fecha2):
        # devuelve un listado de las mediciones de temperatura en el rango recibido por el parametro en formato dd/mm/aaaa
        # temp en gradoc centigrados ordenado por fechas
        pass

    def cantidad_muestras():
        # devuelve la cantidad de muestras de la BD
        # seria la cantidad de nodos que tiene el arbol
        pass