# Archivo de test para realizar pruebas unitarias del modulo1

import unittest
import random
import sys #tuvimos que hacer esto porque este .py esta adentro de tests y funciones esta dentro de modules, lo sacamos de internet
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.funciones import burbuja
from modules.funciones import quicksort
from modules. funciones import residuo

class testPruebaOrden(unittest.TestCase):

    def setUp(self):
        self.lista = [random.randint(10000, 99999) for _ in range(1000)] #creo la lista de 1000 elementos
        self.correcto = sorted(self.lista) #le doy el resultado correcto al que deberia llegar cada algoritmo

    def test_burbuja(self):
        resultado = burbuja(self.lista.copy()) #con el metodo copy() le paso una copia de la lista original creada aleatoriamente entonces no se modifica
        self.assertEqual(resultado, self.correcto) #comparo que el algoritmo funcione correctamente
    
    def test_quicksort(self):
        resultado = quicksort(self.lista.copy())
        self.assertEqual(resultado, self.correcto)
    
    def test_residuo(self):
        resultado = residuo(self.lista.copy())
        self.assertEqual(resultado, self.correcto)

if __name__ == '__main__':
    unittest.main()
    