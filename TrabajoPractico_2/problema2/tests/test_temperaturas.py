import unittest
from modules.temperaturas_DB import Temperaturas_DB
from modules.fecha import Fecha
from random import randint

def auxiliar_minimo_y_maximo(db, fecha1, fecha2):
    minimo_maximo = [41, 0]
    
    for medicion in db:
        if medicion >= fecha1 and medicion <= fecha2:
            if db.devolver_temperatura(medicion) < minimo_maximo[0]:
                minimo_maximo[0] = db.devolver_temperatura(medicion)
                
            if db.devolver_temperatura(medicion) > minimo_maximo[1]:
                minimo_maximo[1] = db.devolver_temperatura(medicion)
            
        
            
    return minimo_maximo

class TestTemperaturasDB(unittest.TestCase):

    def setUp(self):
        self.db = Temperaturas_DB()
        self.db.guardar_temperatura(25.0, "01/01/2024")
        self.db.guardar_temperatura(30.0, "05/01/2024")
        self.db.guardar_temperatura(15.0, "10/01/2024")
        self.db.guardar_temperatura(20.0, "15/01/2024")

    

    def test_guardar_temperatura(self):
        tamanioAntes = len(self.db)
        
        temperatura = randint(0, 40)
        dia = randint(1, 30)    # mejor que dia empiece en 1, para evitar fechas inválidas
        mes = randint(1, 12)
        año = randint(2000, 2022)
        
        clave = Fecha(dia, mes, año)
        
        if clave not in self.db:
            self.db.guardar_temperatura(temperatura, clave)
            self.assertEqual(tamanioAntes + 1, len(self.db))
            tamanioAntes += 1
        else:
            # si ya existe, no debería aumentar el tamaño
            self.db.guardar_temperatura(temperatura, clave)
            self.assertEqual(tamanioAntes, len(self.db))

    def test_devolver_temperatura(self):
        temperatura = randint(0, 40)
        dia = randint(1, 30)    # mejor que dia empiece en 1, para evitar fechas inválidas
        mes = randint(1, 12)
        año = randint(2000, 2022)
        
        clave = Fecha(dia, mes, año)

        self.db.guardar_temperatura(temperatura, clave)
        self.assertEqual(self.db.devolver_temperatura(clave), temperatura)
        
    # def test_max_temp_rango(self):
    #     self.db.borrar()
    #     fecha1=randint(0,50)
    #     fecha2=randint(51,99)
    #     guardo_fecha1=False
    #     guardo_fecha2=False
    #     for i in range (100):
    #         temperatura = randint(0, 40)
    #         dia = randint(1, 30)
    #         mes = randint(1, 12)
    #         año = randint(2000, 2022)
    #         clave=Fecha(dia, mes, año)
    #         if not guardo_fecha1 and i == fecha1:
    #             fecha1= clave
    #             guardo_fecha1 = True
    #         if not guardo_fecha2 and i == fecha2:
    #             fecha2 = clave
    #             guardo_fecha2 = True
    #         self.db.guardar_temperatura(temperatura, clave)
         
    #     if fecha2 < fecha1:
    #                 aux = fecha2
    #                 fecha2 = fecha1
    #                 fecha1 = aux
                    
    #     minimo_maximo = auxiliar_minimo_y_maximo(self.db, fecha1, fecha2)
                
    #     self.assertEqual(minimo_maximo[1], self.db.max_temp_rango(fecha1,fecha2))

    def test_min_temp_rango(self):
        pass

    def test_temp_extremos_rango(self):
        pass


    def test_borrar_temperatura(self):
        self.db.borrar()
        fecha = randint(0, 100)
        guardo_fecha = False
        for i in range(100):
            temperatura = randint(0, 40)
            dia = randint(1, 30)
            mes = randint(1, 12)
            año = randint(2000, 2022)
            clave = Fecha(dia, mes, año)
            if not guardo_fecha and i == fecha:
                fecha = clave
                guardo_fecha = True
            self.db.guardar_temperatura(temperatura, clave)
        fecha_esta = fecha in self.db
        self.assertEqual(fecha_esta, True)
        self.db.borrar_temperatura(fecha)
        fecha_esta = fecha in self.db
        self.assertEqual(fecha_esta, False)



if __name__ == "__main__":
    unittest.main()
