# Archivo de test para realizar pruebas unitarias del modulo1

import unittest
import random
from modules import burbuja
from modules import quicksort
from modules import residuo

class testPruebaOrden(unittest.TestCase):

    def __init__(self):
        self.lista = [random.randint(10000, 99999) for _ in range(1000)] #creo la lista de 1000 elementos
        self.correcto = sorted(self.lista) #le doy el resultado correcto al que deberia llegar cada algoritmo

    def test_burbuja(self):
        resultado = burbuja(self.lista.copy())
        self.assertEqual(resultado, self.correcto)
    
    def test_quicksort(self):
        resultado = quicksort(self.lista.copy())
        self.assertEqual(resultado, self.correcto)
    
    def test_residuo(self):
        resultado = residuo(self.lista.copy())
        self.assertEqual(resultado, self.correcto)

if __name__ == '__main__':
    unittest.main()
    