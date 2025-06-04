
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

    def devolver_temperatura(self, fecha:str):
        #devuelve la medida de temperatura en la fecha determinada
        if type(fecha) == str:
            fecha = fecha.rsplit("/")
            fecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
        else:
            print("No es string !!!  :(")
            return None

        try:
            temp_salida = self.__arbol.obtener(fecha)
            return temp_salida
        
        except KeyError:
            print("No hay una temperatura para esa fecha")
            return None
        
        
    def max_temp_rango(self, fecha1, fecha2):
    # Convierte strings a objetos Fecha si es necesario
        if isinstance(fecha1, str):
            d, m, a = map(int, fecha1.split("/"))
            fecha1 = Fecha(d, m, a)
            
        if isinstance(fecha2, str):
            d, m, a = map(int, fecha2.split("/"))
            fecha2 = Fecha(d, m, a)

        maxima_temperatura = None
        it = Iterador(self.__arbol, fecha1)  # comienza desde fecha1 (o el primer nodo mayor)

        for temperatura in it:
            if temperatura.__valor > maximaTemp:
                maximaTemp = temperatura.__valor
           
            if temperatura.__clave == fecha2:
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
    
    def temp_extremos_rango(self, fecha1:str, fecha2:str):
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


    mediciones.guardar_temperatura(1, "20/12/2000")
    mediciones.guardar_temperatura(3, "21/12/2000")
    mediciones.guardar_temperatura(15, "22/12/2000")
    mediciones.guardar_temperatura(6, "23/12/2000")
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
    
    mediciones.devolver_temperaturas("27/12/2000", "29/12/2000")
    # print("\n----Prueba de mostrar temperaturas----\n")
    # mediciones.devolver_temperaturas()
    
    # print("\n----Prueba de devolver temperatura----\n")
    #  for medicion in mediciones:
    #     print(mediciones.devolver_temperatura(medicion))
    # fecha = input("Introducir fecha dd/mm/aaaa: ")
    # print("La medicion es de: ", mediciones.devolver_temperatura(fecha))
    
    # print("\n----Prueba de max temperaturas----\n")
    # fecha1 = input("Introducir fecha1 dd/mm/aaaa: ")
    # fecha2 = input("Introducir fecha2 dd/mm/aaaa: ") 
    # valores = mediciones.temp_extremos_rango(fecha1, fecha2)
    # print(f"Son:\nMáximo: {valores[1]}\nMínimo: {valores[0]}")
        
    
    # opc = input("¿Desea borrar la base? [S]i o [N]o: ")
    # opc.upper()
    # if opc == 'S':
    #     print("\n----Prueba de borrar BD----\n")
    #     mediciones.borrar()
    #     mediciones.cantidad_muestras()


    