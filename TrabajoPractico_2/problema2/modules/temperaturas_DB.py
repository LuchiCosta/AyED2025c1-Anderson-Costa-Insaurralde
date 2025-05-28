import datetime
from modules import Arbol_binario_equilibrado
class temperaturas_DB:
    def __init__(self):
        self.__arbol = Arbol_binario_equilibrado()
    
    def traductor_fecha(self, fecha):
        # Método privado auxiliar para convertir una cadena de fecha a un objeto datetime.date
        return datetime.datetime.strptime(fecha, '%d/%m/%Y').date() # Usa strptime para traducir la cadena y .date() para obtener solo la fecha
    
    def guardar_temperatura(self, temperatura, fecha):
        # guarda la medida de temperatura asociada a la fecha
        fecha = self.traductor_fecha(fecha) 
        # Intenta obtener el nodo si la fecha ya existe para actualizarlo
        nodo_existente = self.__arbol._obtener(fecha, self.__arbol.raiz)
        if nodo_existente: # Si la fecha ya existe en el árbol
            nodo_existente.valor = temperatura # Actualiza el valor de la temperatura en ese nodo
            print(f"Temperatura para la fecha {fecha} actualizada a {temperatura:.2f}ºC.")
        else: # Si la fecha no existe
            self.__arbol.agregar(fecha, temperatura) # Agrega la nueva fecha y temperatura al árbol
            print(f"Temperatura {temperatura:.2f}ºC guardada para la fecha {fecha}.")

    def devolver_temperatura(self, fecha):
        #devuelve la medida de temperatura en la fecha determinada
        fecha = self.traductor_fecha(fecha) 
        temperatura = self.__arbol.obtener(fecha) # Obtiene la temperatura del árbol
        if temperatura is not None: # Si se encontró una temperatura
            return f"Temperatura para {fecha}: {temperatura:.2f} ºC" # Retorna la temperatura formateada, (anotado en notas la explicacion)
        else: 
            return f"No se encontró temperatura para la fecha {fecha}" 

    def max_temp_rango(self, fecha1, fecha2):
        # devuelde la temperatura maxima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es meno a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        fecha1 = self.traductor_fecha(fecha1) 
        fecha2 = self.traductor_fecha(fecha2) 
        if fecha1 >= fecha2: # Valida que la primera fecha sea menor que la segunda
            raise ValueError("fecha1 debe ser menor que fecha2") # Lanza un error si el rango es inválido
        
        max_temp = self.__arbol.get_max_in_range(fecha1, fecha2, self.__arbol.raiz, None) # Llama al método del árbol para buscar el máximo
        if max_temp is not None: # Si se encontró una temperatura máxima
            return f"Temperatura máxima entre {fecha1} y {fecha2}: {max_temp:.2f} ºC" # Retorna el resultado formateado
        else: # Si no hay datos en el rango
            return f"No hay datos de temperatura en el rango {fecha1} - {fecha2}" 

    def min_temp_rango(self, fecha1, fecha2):
        # devuelde la temperatura minima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es menor a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        fecha1 = self.traductor_fecha(fecha1)
        fecha2 = self.traductor_fecha(fecha2)
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")

        min_temp = self.__arbol.min_temp(fecha1, fecha2, self.__arbol.raiz, None) # no me toma el metodo no se porque
        if min_temp is not None:
            return f"Temperatura mínima entre {fecha1} y {fecha2}: {min_temp:.2f} ºC"
        else:
            return f"No hay datos de temperatura en el rango {fecha1} - {fecha2}"

    def temp_extremos_rango(self, fecha1, fecha2):
        # devuelve la temperatura minima y maxima entre los rangos fecha1 y fecha2 inclusive, fecha1 menor que fecha2
        fecha1 = self.traductor_fecha(fecha1)
        fecha2 = self.traductor_fecha(fecha2)
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")

        max_temp = self.__arbol.max_temp(fecha1, fecha2, self.__arbol.raiz, None) # no me toma el metodo q viene del arbol binario
        min_temp = self.__arbol.min_temp(fecha1, fecha2, self.__arbol.raiz, None) 

        if max_temp is not None and min_temp is not None: # Si se encontraron datos en el rango
            return (f"Extremos de temperatura entre {fecha1} y {fecha2}: "
                    f"Mínima: {min_temp:.2f} ºC, Máxima: {max_temp:.2f} ºC") # Retorna ambos valores formateados
        else:
            return f"No hay datos de temperatura en el rango {fecha1} - {fecha2}" 

    def borrar_temperatura(self, fecha):
        # recibe una fecha y elimina del arbol la medicion correspondiente a esa fecha
        # borra el nodo del arbol (ver en el libro)
        fecha = self.traductor_fecha(fecha) # Convierte la fecha string a objeto datetime.date
        try: # Intenta eliminar el nodo
            self.__arbol.eliminar(fecha) # Llama al método de eliminación del árbol
            print(f"Temperatura para la fecha {fecha} eliminada exitosamente.") # Mensaje de éxito
        except KeyError as e: # Captura la excepción si la clave no se encuentra
            print(f"Error al eliminar: {e}") # Imprime el error
        except Exception as e: # Captura cualquier otra excepción inesperada
            print(f"Ocurrió un error inesperado al eliminar: {e}") # Imprime el error

    def devolver_temperaturas(self, fecha1, fecha2):
        # devuelve un listado de las mediciones de temperatura en el rango recibido por el parametro en formato dd/mm/aaaa
        # temp en gradoc centigrados ordenado por fechas
        fecha1 = self.traductor_fecha(fecha1)
        fecha2 = self.traductor_fecha(fecha2)
        if fecha1 >= fecha2:
            raise ValueError("fecha1 debe ser menor que fecha2")

        resultados = [] 
        # Llama al método del árbol para llenar la lista con las temperaturas en el rango
        self.__arbol.temperaturas_rango(fecha1, fecha2, self.__arbol.raiz, resultados) #de nuevo no me toma el metodo
        if resultados: 
            print(f"Temperaturas en el rango {fecha1} - {fecha2}:")
            return "\n".join(resultados) # Une los resultados con saltos de línea y los retorna
        else: 
            return f"No se encontraron temperaturas en el rango {fecha1} - {fecha2}" 

    def cantidad_muestras(self):
        # devuelve la cantidad de muestras de la BD
        # seria la cantidad de nodos que tiene el arbol
        return f"Cantidad de muestras en la base de datos: {self.__arbol.tamano}" 
