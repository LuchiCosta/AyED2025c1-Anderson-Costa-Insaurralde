from modules.Arbol_binario_equilibrado import ArbolBinarioEquilibrado
from modules.fecha import Fecha
from modules.iterador import Iterador
from random import randint

class Temperaturas_DB:
    def __init__(self):
        self.__arbol = ArbolBinarioEquilibrado()

    def devolver_raiz(self):
        return self.__arbol.raiz


    def guardar_temperatura(self, temperatura:int, fecha:str):
        # guarda la medida de temperatura asociada a la fecha
        if type(fecha) == str:
            print("fecha paso")
            fecha = fecha.rsplit("/") # right space split - lo separa a la derecha
            fecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
            print("La fecha que se guardo es:",  fecha)
        else:
            print(" No se guardo nada :(")
            
        self.__arbol.agregar(fecha, temperatura)

    def devolver_temperatura(self, fecha):
        # Acepta tanto string como objeto Fecha
        if isinstance(fecha, str):
            fecha = fecha.rsplit("/")
            fecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
        elif not isinstance(fecha, Fecha):
            print("Tipo de fecha no válido")
            return None

        try:
            temp_salida = self.__arbol.obtener(fecha)
            return temp_salida
        except KeyError:
            print("No hay una temperatura para esa fecha")
            return None
        
        
    def max_temp_rango(self, fecha1, fecha2):
    # Convierte strings a objetos Fecha si es necesario
        if type(fecha1) == str:
            fecha1 = fecha1.rsplit("/")
            fecha1 = Fecha(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
            
        if type(fecha2) == str:
            fecha2 = fecha2.rsplit("/")
            fecha2 = Fecha(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))
        
        maxima_temperatura = None
        it = Iterador(self.__arbol, fecha1)

        for nodo in it:
        # Suponiendo que nodo.clave y nodo.valor existen
            if fecha1 <= nodo.clave <= fecha2:
                if (maxima_temperatura is None) or (nodo.valor > maxima_temperatura):
                    maxima_temperatura = nodo.valor
            # No cortar el bucle aquí

        return maxima_temperatura


    def min_temp_rango(self, fecha1, fecha2):
        if type(fecha1) == str:
            fecha1 = fecha1.rsplit("/")
            fecha1 = Fecha(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
        if type(fecha2) == str:
            fecha2 = fecha2.rsplit("/")
            fecha2 = Fecha(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))

        minima_temperatura = None
        fecha_actual = fecha1
        while fecha_actual <= fecha2:
            temp = self.devolver_temperatura(fecha_actual)
            if temp is not None:
                if (minima_temperatura is None) or (temp < minima_temperatura):
                    minima_temperatura = temp
            fecha_actual = fecha_actual.sumar_dias(1)

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
    
    def borrar_temperatura(self, fecha:str):
        # recibe una fecha y elimina del arbol la medicion correspondiente a esa fecha
        # borra el nodo del arbol (ver en el libro)
        if type(fecha) == str:
            print("fecha paso")
            fecha = fecha.rsplit("/")
            fecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
            
        if fecha in self.__arbol:
            print("entra")
            self.__arbol.eliminar(fecha)
        else:
            print("No hay una temperatura para esa fecha")

    def devolver_temperaturas(self, fecha1, fecha2):
        # devuelve un listado de las mediciones de temperatura en el rango recibido 
        # por el parametro en formato dd/mm/aaaa
        # temp en gradoc centigrados ordenado por fechas
        fechas_en_rango = []

        if type(fecha1) == str:
            fecha1 = fecha1.rsplit("/")
            fecha1 = Fecha(int(fecha1[0]), int(fecha1[1]), int(fecha1[2]))
            
        if type(fecha2) == str:
            fecha2 = fecha2.rsplit("/")
            fecha2 = Fecha(int(fecha2[0]), int(fecha2[1]), int(fecha2[2]))

        fecha_actual = fecha1

        while fecha_actual <= fecha2:
            temp = self.devolver_temperatura(fecha_actual)
            if temp is not None:
                fechas_en_rango.append((fecha_actual, temp))
            fecha_actual = fecha_actual.sumar_dias(1)
        return fechas_en_rango

    def cantidad_muestras(self):
        # devuelve la cantidad de muestras de la BD
        # seria la cantidad de nodos que tiene el arbol
        return f"Cantidad de muestras en la base de datos: {self.__arbol.tamano}" 
    
    def borrar (self):
        # borra el arbol
        self.__arbol = ArbolBinarioEquilibrado()
    

    def __len__(self):
        return self.__arbol.tamano
    
    def __iter__(self):
            return iter(self.__arbol)
    
    def __contains__(self, clave):
        return self.devolver_temperatura(clave) is not None
    
if __name__ == "__main__":
    mediciones = Temperaturas_DB()


    mediciones.guardar_temperatura(15, "20/12/2000")
    mediciones.guardar_temperatura(3, "21/12/2000")
    mediciones.guardar_temperatura(5, "22/12/2000")
    mediciones.guardar_temperatura(2, "23/12/2000")
    mediciones.guardar_temperatura(-8, "24/12/2000")
    mediciones.guardar_temperatura(12, "25/12/2000")
    mediciones.guardar_temperatura(37, "26/12/2000")
    mediciones.guardar_temperatura(20, "27/12/2000")
    mediciones.guardar_temperatura(-1, "28/12/2000")
    mediciones.guardar_temperatura(0, "29/12/2000")

    print("comprobamos que funciona: ")
    
    print(mediciones.cantidad_muestras())
    print("La temperatura es de :")
    print( mediciones.devolver_temperatura("26/12/2000"))
    
    mediciones.borrar_temperatura("22/12/2000")
    print(mediciones.cantidad_muestras())
    
    resultados = mediciones.devolver_temperaturas("25/12/2000", "29/12/2000")
    print("Las temperaturas en el rango son:")
    for fecha, temp in resultados:
        print(f"{fecha}: {temp}°C")

    print("La temperatura máxima en el rango es:")
    print(mediciones.max_temp_rango("25/12/2000", "29/12/2000"))
    
    print("La temperatura minima en el rango es:")
    print(mediciones.min_temp_rango("25/12/2000", "29/12/2000"))
    
    valores = mediciones.temp_extremos_rango("20/12/2000", "23/12/2000")
    print(f"Temperatura mínima: {valores[0]}")
    print(f"Temperatura máxima: {valores[1]}")




