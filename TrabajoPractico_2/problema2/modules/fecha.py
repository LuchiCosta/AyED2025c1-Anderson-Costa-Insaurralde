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

if __name__ == "__main__":
    fecha1 = Fecha(12, 10, 2008)
    fecha2 = Fecha(12, 10, 2006)
    
    print(fecha1 >fecha2)    