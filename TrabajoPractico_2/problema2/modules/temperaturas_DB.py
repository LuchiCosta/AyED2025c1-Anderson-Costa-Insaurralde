import datetime
from modules.Arbol_binario_equilibrado import ArbolBinarioEquilibrado
class Temperaturas_DB:
    def __init__(self):
        self.__arbol = ArbolBinarioEquilibrado()
    
    def traductor_fecha(self, fecha):
        # Método privado auxiliar para convertir una cadena de fecha a un objeto datetime.date
        return datetime.datetime.strptime(fecha, '%d/%m/%Y').date() # Usa strptime para traducir la cadena y .date() para obtener solo la fecha
    
    def guardar_temperatura(self, temperatura, fecha):
        # guarda la medida de temperatura asociada a la fecha
        try:
            fecha = self.traductor_fecha(fecha)
        except ValueError:
            return "Error: formato de fecha inválido. Use dd/mm/aaaa."

    # Intenta obtener el nodo si la fecha ya existe para actualizarlo
        nodo_existente = self.__arbol._obtener(fecha, self.__arbol.raiz)
        if nodo_existente:
            nodo_existente.valor = temperatura
            print(f"Temperatura para la fecha {fecha} actualizada a {temperatura:.2f}ºC.")
        else:
            self.__arbol.agregar(fecha, temperatura)
            print(f"Temperatura {temperatura:.2f}ºC guardada para la fecha {fecha}.")

    def devolver_temperatura(self, fecha):
        #devuelve la medida de temperatura en la fecha determinada
        try:
            fecha_obj = self.traductor_fecha(fecha)
        except ValueError:
            return "Error: formato de fecha inválido. Use dd/mm/aaaa."

        nodo = self.__arbol._obtener(fecha_obj, self.__arbol.raiz)
        if nodo:
            fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
            return f"Temperatura para {fecha_formateada}: {nodo.valor:.2f} ºC"
        else:
            return f"No se encontró temperatura para la fecha {fecha}"
        
    def max_temp_rango(self, fecha1, fecha2):
        # devuelde la temperatura maxima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es meno a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        try:
            fecha1 = self.traductor_fecha(fecha1)
            fecha2 = self.traductor_fecha(fecha2)
        except ValueError:
            return "Error: formato de fecha inválido. Use dd/mm/aaaa."

        if fecha1 > fecha2:
            return "Error: la fecha inicial debe ser menor que la fecha final."

        temperaturas = []
        self.__arbol.temperaturas_rango(fecha1, fecha2, self.__arbol.raiz, temperaturas)

        if temperaturas:
            max_temp = max(float(t.split(": ")[1].split()[0]) for t in temperaturas)
            return f"Temperatura máxima en el rango: {max_temp:.2f} ºC"
        else:
            return f"No se encontraron temperaturas en el rango {fecha1.strftime('%d/%m/%Y')} - {fecha2.strftime('%d/%m/%Y')}"

    def min_temp_rango(self, fecha1, fecha2):
        # devuelde la temperatura minima entre los rangos de fecha1 y fecha2 inclusive, fecha1 es menor a fecha2. no implica que los
        # intervalos del rango deban ser fechas incluidas previamente en el arbol
        try:
            fecha1 = self.traductor_fecha(fecha1)
            fecha2 = self.traductor_fecha(fecha2)
        except ValueError:
            return "Error: formato de fecha inválido. Use dd/mm/aaaa."

        if fecha1 > fecha2:
            return "Error: la fecha inicial debe ser menor que la fecha final."

        resultados = []
        self.__arbol.temperaturas_rango(fecha1, fecha2, self.__arbol.raiz, resultados)

        if resultados:
            temperaturas = [float(r.split(":")[1].split()[0]) for r in resultados]
            temp_min = min(temperaturas)
            return f"Temperatura mínima entre {fecha1.strftime('%d/%m/%Y')} y {fecha2.strftime('%d/%m/%Y')}: {temp_min:.2f} ºC"
        else:
            return f"No hay temperaturas registradas entre {fecha1.strftime('%d/%m/%Y')} y {fecha2.strftime('%d/%m/%Y')}"

    def temp_extremos_rango(self, fecha1, fecha2):
        # devuelve la temperatura minima y maxima entre los rangos fecha1 y fecha2 inclusive, fecha1 menor que fecha2
        try:
            fecha1 = self.traductor_fecha(fecha1)
            fecha2 = self.traductor_fecha(fecha2)
        except ValueError:
            return "Error: formato de fecha inválido. Use dd/mm/aaaa."

        if fecha1 > fecha2:
            return "Error: la fecha inicial debe ser menor que la fecha final."

        resultados = []
        self.__arbol.temperaturas_rango(fecha1, fecha2, self.__arbol.raiz, resultados)

        if resultados:
            temperaturas = [float(r.split(":")[1].split()[0]) for r in resultados]
            temp_min = min(temperaturas)
            temp_max = max(temperaturas)
            return (f"Extremos de temperatura entre {fecha1.strftime('%d/%m/%Y')} y {fecha2.strftime('%d/%m/%Y')}: "
                    f"Mínima: {temp_min:.2f} ºC, Máxima: {temp_max:.2f} ºC")
        else:
            return f"No hay temperaturas registradas entre {fecha1.strftime('%d/%m/%Y')} y {fecha2.strftime('%d/%m/%Y')}" 

    def borrar_temperatura(self, fecha):
        # recibe una fecha y elimina del arbol la medicion correspondiente a esa fecha
        # borra el nodo del arbol (ver en el libro)
        try:
            fecha = self.traductor_fecha(fecha)
        except ValueError:
            return "Error: formato de fecha inválido. Use dd/mm/aaaa."

        nodo = self.__arbol._obtener(fecha, self.__arbol.raiz)
        if nodo:
            self.__arbol.eliminar(fecha)
            return f"Temperatura para la fecha {fecha.strftime('%d/%m/%Y')} eliminada exitosamente."
        else:
            return f"No se encontró temperatura para la fecha {fecha.strftime('%d/%m/%Y')}"

    def devolver_temperaturas(self, fecha1, fecha2):
        # devuelve un listado de las mediciones de temperatura en el rango recibido por el parametro en formato dd/mm/aaaa
        # temp en gradoc centigrados ordenado por fechas
        try:
            fecha1 = self.traductor_fecha(fecha1)
            fecha2 = self.traductor_fecha(fecha2)
        except ValueError:
            return "Error: formato de fecha inválido. Use dd/mm/aaaa."

        if fecha1 >= fecha2:
            return "Error: la fecha inicial debe ser menor que la fecha final."

        resultados = []
        self.__arbol.temperaturas_rango(fecha1, fecha2, self.__arbol.raiz, resultados)

        if resultados:
            return "\n".join(resultados)
        else:
            return f"No se encontraron temperaturas en el rango {fecha1.strftime('%d/%m/%Y')} - {fecha2.strftime('%d/%m/%Y')}"

    def cantidad_muestras(self):
        # devuelve la cantidad de muestras de la BD
        # seria la cantidad de nodos que tiene el arbol
        return f"Cantidad de muestras en la base de datos: {self.__arbol.tamano}" 
