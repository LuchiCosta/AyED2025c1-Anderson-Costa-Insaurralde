import unittest
from modules.temperaturas_DB import Temperaturas_DB
from modules.fecha import Fecha
from random import randint

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
            


if __name__ == "__main__":
    unittest.main()