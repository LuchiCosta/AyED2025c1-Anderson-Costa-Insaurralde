import datetime
from modules.Arbol_binario_equilibrado import ArbolBinarioEquilibrado
from modules.fecha import Fecha
from modules.iterador import Iterador

class Temperaturas_DB:
    def __init__(self):
        self.__arbol = ArbolBinarioEquilibrado()
    
    def guardar_temperatura(self, temperatura, fecha):
        # guarda la medida de temperatura asociada a la fecha
        if type(fecha) == str:
            fecha = fecha.rsplit("/") # right space split - lo separa a la derecha
            fecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
            
        self.__arbol.agregar(fecha, temperatura)

    def devolver_temperatura(self, fecha):
        #devuelve la medida de temperatura en la fecha determinada
        if type(fecha) == str:
            fecha = fecha.rsplit("/")
            fecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))

        if fecha in self.__arbol:
            return self.__arbol[fecha]
        else:
            print("No hay una temperatura para esa fecha")
        
    def max_temp_rango(self, fecha1, fecha2):
        # devuelve la temperatura maxima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es meno a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        if type(fecha1) == str:
            fecha1 = fecha1.rsplit("/")
            fecha1 = Fecha(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
            
        if type(fecha2) == str:
            fecha2 = fecha2.rsplit("/")
            fecha2 = Fecha(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))

        iterador = Iterador(self.__arbol, fecha1)
        maxima_temperatura = self.devolver_temperatura(fecha1)

        for temperatura in iterador:
            if temperatura.__valor > maxima_temperatura: # si la temperatura es mayor a la que asigne
                maxima_temperatura = temperatura.__valor # cambio el valor de mi maxima temperatura
            
            if temperatura.__clave == fecha2: # si la fecha es igual a la fecha 2
                break

        return maxima_temperatura

    def min_temp_rango(self, fecha1, fecha2):
        # devuelde la temperatura minima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es menor a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        if type(fecha1) == str:
            fecha1 = fecha1.rsplit("/")
            fecha1 = Fecha(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
            
        if type(fecha2) == str:
            fecha2 = fecha2.rsplit("/")
            fecha2 = Fecha(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))

        iterador = Iterador(self.__arbol, fecha1)
        minima_temperatura = self.devolver_temperatura(fecha1)

        for temperatura in iterador:
            if temperatura.__valor < minima_temperatura: # si la temperatura es mayor a la que asigne
                minima_temperatura = temperatura.__valor # cambio el valor de mi maxima temperatura
            
            if temperatura.__clave == fecha2: # si la fecha es igual a la fecha 2
                break

        return minima_temperatura
    
    def temp_extremos_rango(self, fecha1, fecha2):
        # devuelve la temperatura minima y maxima entre los rangos fecha1 y fecha2 inclusive, fecha1 menor que fecha2
        if type(fecha1) == str:
            fecha1 = fecha1.rsplit("/")
            fecha1 = Fecha(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
            
        if type(fecha2) == str:
            fecha2 = fecha2.rsplit("/")
            fecha2 = Fecha(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))
            
        extremos = []
        
        extremos.append(self.min_temp_rango(fecha1, fecha2))
        extremos.append(self.max_temp_rango(fecha1, fecha2))
        
        return extremos
    
    def borrar_temperatura(self, fecha):
        # recibe una fecha y elimina del arbol la medicion correspondiente a esa fecha
        # borra el nodo del arbol (ver en el libro)
        if type(fecha) == str:
            fecha = fecha.rsplit("/")
            fecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
            
        if fecha in self.__arbol:
            self.__arbol.eliminar(fecha)
        else:
            print("No hay una temperatura para esa fecha")

    def devolver_temperaturas(self, fecha1, fecha2):
        # devuelve un listado de las mediciones de temperatura en el rango recibido por el parametro en formato dd/mm/aaaa
        # temp en gradoc centigrados ordenado por fechas
        fechas_en_rango = []

        for fecha_str in self.__arbol:
            # Convertimos el string "dd/mm/aaaa" a un objeto Fecha
            dia, mes, anio = map(int, fecha_str.split("/")) # convierte los valores a enteros
            fecha = Fecha(dia, mes, anio)

            if fecha1 <= fecha <= fecha2:
                fechas_en_rango.append(fecha)

        if fechas_en_rango:
            # Ordenar las fechas usando los operadores definidos en tu clase Fecha
            for fecha in sorted(fechas_en_rango): # sorted ordena
                print(f"{fecha}: {self.devolver_temperatura(str(fecha))} °C")
        else:
            print("No hay mediciones en este rango")
                  
    def cantidad_muestras(self):
        # devuelve la cantidad de muestras de la BD
        # seria la cantidad de nodos que tiene el arbol
        return f"Cantidad de muestras en la base de datos: {self.__arbol.tamano}" 
