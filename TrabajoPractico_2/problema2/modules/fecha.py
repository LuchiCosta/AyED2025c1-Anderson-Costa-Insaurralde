from datetime import date, timedelta

class Fecha:
    def __init__(self, dia, mes, anio):
        self._dia = dia
        self._mes = mes
        self._anio = anio
    
    @property
    def dia(self):
        # getter del dia
        return self._dia
    
    @property 
    def mes(self):
        return self._mes
    
    @property
    def anio(self):
        return self._anio
    
    def __str__(self): # string 
        # permite representacion como string
        return f"{self._dia}/{self._mes}/{self._anio}"
    
    def __lt__(self, fecha2): # lesser than 
        # permite usar el operador <
        if self._anio != fecha2.anio:
            return self._anio < fecha2.anio
        else:
            if self._mes == fecha2.mes:
                return self._dia < fecha2.dia
            else:
                return self._mes < fecha2.mes
    
    def __gt__(self, fecha2): # greater than 
        # permite usar el >
        if self._anio != fecha2.anio:
            return self._anio > fecha2.anio
        else:
            if self._mes == fecha2.mes:
                return self._dia > fecha2.dia
            else:
                return self._mes > fecha2.mes
    
    def __eq__(self, fecha2): # equal
        # permite usar ==
        if self._anio == fecha2.anio:
            if self._mes == fecha2.mes:
                if self._dia == fecha2.dia:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __le__(self, fecha2): # less or equal
        # permite usar <=
        return self < fecha2 or self == fecha2

    def __ge__(self, fecha2):
        # permite usar el >=
       return self > fecha2 or self == fecha2
    
    def __ne__(self, fecha2): # not equal
        # permite usar el !=
        if self == fecha2:
            return True
        else:
            return False

    def to_date(self):
        """Convierte el objeto Fecha a un objeto datetime.date"""
        return date(self._anio, self._mes, self._dia)

    @classmethod
    def from_date(cls, d):
        """Crea un objeto Fecha desde un objeto datetime.date"""
        return cls(d.day, d.month, d.year)

    def sumar_dias(self, dias):
        """Devuelve un nuevo objeto Fecha sumando 'dias' días"""
        nueva_fecha = self.to_date() + timedelta(days=dias)
        return Fecha.from_date(nueva_fecha)

if __name__ == "__main__":
    fecha1 = Fecha(12, 10, 2006)
    fecha2 = Fecha(17, 10, 2006)
    
    print(fecha1 ==fecha2)
    #probamos que funcione sumar los dias 
    lista_fechas = []
    while fecha1<= fecha2:
        lista_fechas.append(str(fecha1))
        fecha1 = fecha1.sumar_dias(1)
    print(lista_fechas)