import unittest
from modules.temperaturas_DB import Temperaturas_DB
from modules.fecha import Fecha
from random import randint

class TestTemperaturasDB(unittest.TestCase):

    def setUp(self):
        self.db = Temperaturas_DB()

    def test_guardar_y_devolver_temperatura(self):
        """
        Verifica la funcionalidad básica de guardar y devolver una temperatura.
        """
        self.db.guardar_temperatura(25.5, "01/01/2023")
        self.assertEqual(self.db.devolver_temperatura("01/01/2023"), "Temperatura para 01/01/2023: 25.50 ºC")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 1")

        self.db.guardar_temperatura(18.0, "15/01/2023")
        self.assertEqual(self.db.devolver_temperatura("15/01/2023"), "Temperatura para 15/01/2023: 18.00 ºC")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 2")

    def test_actualizar_temperatura_existente(self):
        """
        Verifica que se pueda actualizar la temperatura para una fecha existente.
        """
        self.db.guardar_temperatura(20.0, "05/01/2023")
        self.assertEqual(self.db.devolver_temperatura("05/01/2023"), "Temperatura para 05/01/2023: 20.00 ºC")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 1")

        self.db.guardar_temperatura(22.5, "05/01/2023") # Actualiza la misma fecha
        self.assertEqual(self.db.devolver_temperatura("05/01/2023"), "Temperatura para 05/01/2023: 22.50 ºC")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 1") # El tamaño no debe cambiar

    def test_devolver_temperatura_no_existente(self):
        """
        Verifica el comportamiento al intentar devolver una temperatura que no existe.
        """
        self.assertEqual(self.db.devolver_temperatura("10/02/2023"), "No se encontró temperatura para la fecha 10/02/2023")
        self.db.guardar_temperatura(10.0, "01/01/2024")
        self.assertEqual(self.db.devolver_temperatura("10/02/2023"), "No se encontró temperatura para la fecha 10/02/2023")

    def test_max_temp_rango(self):
        """
        Verifica la obtención de la temperatura máxima en un rango.
        """
        self.db.guardar_temperatura(20.0, "01/03/2023")
        self.db.guardar_temperatura(28.0, "05/03/2023")
        self.db.guardar_temperatura(15.0, "10/03/2023")
        self.db.guardar_temperatura(22.0, "15/03/2023")

        self.assertEqual(self.db.max_temp_rango("01/03/2023", "10/03/2023"), "Temperatura máxima entre 01/03/2023 y 10/03/2023: 28.00 ºC")
        self.assertEqual(self.db.max_temp_rango("06/03/2023", "16/03/2023"), "Temperatura máxima entre 06/03/2023 y 16/03/2023: 22.00 ºC")
        self.assertEqual(self.db.max_temp_rango("01/03/2023", "01/03/2023"), "Temperatura máxima entre 01/03/2023 y 01/03/2023: 20.00 ºC")
        
        # Rango sin datos
        self.assertEqual(self.db.max_temp_rango("20/03/2023", "25/03/2023"), "No hay datos de temperatura en el rango 20/03/2023 - 25/03/2023")
        # Rango inválido
        self.assertIn("Error", self.db.max_temp_rango("10/03/2023", "01/03/2023"))


    def test_min_temp_rango(self):
        """
        Verifica la obtención de la temperatura mínima en un rango.
        """
        self.db.guardar_temperatura(20.0, "01/03/2023")
        self.db.guardar_temperatura(28.0, "05/03/2023")
        self.db.guardar_temperatura(15.0, "10/03/2023")
        self.db.guardar_temperatura(22.0, "15/03/2023")

        self.assertEqual(self.db.min_temp_rango("01/03/2023", "10/03/2023"), "Temperatura mínima entre 01/03/2023 y 10/03/2023: 15.00 ºC")
        self.assertEqual(self.db.min_temp_rango("06/03/2023", "16/03/2023"), "Temperatura mínima entre 06/03/2023 y 16/03/2023: 15.00 ºC")
        self.assertEqual(self.db.min_temp_rango("05/03/2023", "05/03/2023"), "Temperatura mínima entre 05/03/2023 y 05/03/2023: 28.00 ºC")

        # Rango sin datos
        self.assertEqual(self.db.min_temp_rango("20/03/2023", "25/03/2023"), "No hay datos de temperatura en el rango 20/03/2023 - 25/03/2023")
        # Rango inválido
        self.assertIn("Error", self.db.min_temp_rango("10/03/2023", "01/03/2023"))


    def test_temp_extremos_rango(self):
        """
        Verifica la obtención de temperaturas extremas (mínima y máxima) en un rango.
        """
        self.db.guardar_temperatura(10.0, "01/01/2024")
        self.db.guardar_temperatura(30.0, "05/01/2024")
        self.db.guardar_temperatura(5.0, "10/01/2024")
        self.db.guardar_temperatura(25.0, "15/01/2024")

        expected = "Extremos de temperatura entre 01/01/2024 y 15/01/2024: Mínima: 5.00 ºC, Máxima: 30.00 ºC"
        self.assertEqual(self.db.temp_extremos_rango("01/01/2024", "15/01/2024"), expected)

        # Rango más pequeño
        expected_small_range = "Extremos de temperatura entre 06/01/2024 y 12/01/2024: Mínima: 5.00 ºC, Máxima: 5.00 ºC"
        self.assertEqual(self.db.temp_extremos_rango("06/01/2024", "12/01/2024"), expected_small_range)

        # Rango sin datos
        self.assertEqual(self.db.temp_extremos_rango("20/01/2024", "25/01/2024"), "No hay datos de temperatura en el rango 20/01/2024 - 25/01/2024")
        # Rango inválido
        self.assertIn("Error", self.db.temp_extremos_rango("15/01/2024", "01/01/2024"))

    def test_borrar_temperatura(self):
        """
        Verifica la eliminación de temperaturas.
        """
        self.db.guardar_temperatura(20.0, "01/01/2023")
        self.db.guardar_temperatura(22.0, "02/01/2023")
        self.db.guardar_temperatura(24.0, "03/01/2023")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 3")

        self.assertEqual(self.db.borrar_temperatura("02/01/2023"), "Temperatura para la fecha 02/01/2023 eliminada exitosamente.")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 2")
        self.assertEqual(self.db.devolver_temperatura("02/01/2023"), "No se encontró temperatura para la fecha 02/01/2023")

        self.assertEqual(self.db.borrar_temperatura("01/01/2023"), "Temperatura para la fecha 01/01/2023 eliminada exitosamente.")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 1")

        self.assertEqual(self.db.borrar_temperatura("03/01/2023"), "Temperatura para la fecha 03/01/2023 eliminada exitosamente.")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 0")

        # Intentar borrar una fecha que no existe
        self.assertEqual(self.db.borrar_temperatura("10/01/2023"), "No se encontró temperatura para la fecha 10/01/2023. No se pudo eliminar.")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 0")

        # Intentar borrar con formato de fecha incorrecto
        self.assertIn("Error", self.db.borrar_temperatura("fecha_invalida"))


    def test_devolver_temperaturas_en_rango(self):
        """
        Verifica la obtención de todas las temperaturas en un rango, ordenadas.
        """
        self.db.guardar_temperatura(20.0, "01/01/2023")
        self.db.guardar_temperatura(28.0, "05/01/2023")
        self.db.guardar_temperatura(15.0, "10/01/2023")
        self.db.guardar_temperatura(22.0, "15/01/2023")
        self.db.guardar_temperatura(18.0, "03/01/2023")
        self.db.guardar_temperatura(26.0, "12/01/2023")

        expected_full_range = (
            "01/01/2023: 20.00 ºC\n"
            "03/01/2023: 18.00 ºC\n"
            "05/01/2023: 28.00 ºC\n"
            "10/01/2023: 15.00 ºC\n"
            "12/01/2023: 26.00 ºC\n"
            "15/01/2023: 22.00 ºC"
        )
        self.assertEqual(self.db.devolver_temperaturas("01/01/2023", "15/01/2023"), expected_full_range)

        expected_partial_range = (
            "03/01/2023: 18.00 ºC\n"
            "05/01/2023: 28.00 ºC\n"
            "10/01/2023: 15.00 ºC"
        )
        self.assertEqual(self.db.devolver_temperaturas("03/01/2023", "10/01/2023"), expected_partial_range)

        # Rango de un solo día
        self.assertEqual(self.db.devolver_temperaturas("05/01/2023", "05/01/2023"), "05/01/2023: 28.00 ºC")

        # Rango sin datos
        self.assertEqual(self.db.devolver_temperaturas("20/01/2023", "25/01/2023"), "No se encontraron temperaturas en el rango 20/01/2023 - 25/01/2023")
        
        # Rango inválido
        self.assertIn("Error", self.db.devolver_temperaturas("15/01/2023", "01/01/2023"))


    def test_cantidad_muestras(self):
        """
        Verifica que la cuenta de muestras sea correcta.
        """
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 0")
        self.db.guardar_temperatura(10.0, "01/01/2025")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 1")
        self.db.guardar_temperatura(12.0, "02/01/2025")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 2")
        self.db.borrar_temperatura("01/01/2025")
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 1")
        self.db.guardar_temperatura(15.0, "02/01/2025") # Actualiza, no añade
        self.assertEqual(self.db.cantidad_muestras(), "Cantidad de muestras en la base de datos: 1")


    def test_manejo_formato_fecha_invalido(self):
        """
        Verifica que se manejen correctamente los formatos de fecha inválidos.
        """
        self.assertIn("Error", self.db.guardar_temperatura(20.0, "01-01-2023"))
        self.assertIn("Error", self.db.devolver_temperatura("2023/01/01"))
        self.assertIn("Error", self.db.max_temp_rango("invalido", "01/01/2024"))
        self.assertIn("Error", self.db.min_temp_rango("01/01/2024", "invalido"))
        self.assertIn("Error", self.db.temp_extremos_rango("invalido", "01/01/2024"))
        self.assertIn("Error", self.db.borrar_temperatura("formato incorrecto"))
        self.assertIn("Error", self.db.devolver_temperaturas("01-01-2024", "05/01/2024"))

    def test_arbol_balanceo_avl(self):
        """
        Un test más avanzado para verificar que el árbol AVL se mantenga balanceado
        después de varias inserciones y eliminaciones.
        Este test se enfoca en el comportamiento interno del AVL, no solo la interfaz.
        """
        dates = [
            "15/05/2023", "10/05/2023", "20/05/2023", "05/05/2023",
            "12/05/2023", "18/05/2023", "25/05/2023", "08/05/2023",
            "13/05/2023", "17/05/2023", "22/05/2023", "28/05/2023"
        ]
        temps = [i * 1.0 for i in range(len(dates))]

        for i, date_str in enumerate(dates):
            self.db.guardar_temperatura(temps[i], date_str)
            # Después de cada inserción, se puede verificar el balanceo.
            # Una forma simple es verificar que todos los nodos tienen factorEquilibrio en [-1, 0, 1]
            self._assert_avl_balance(self.db._Temperaturas_DB__arbol.raiz)
        
        self.assertEqual(self.db.cantidad_muestras(), f"Cantidad de muestras en la base de datos: {len(dates)}")

        # Eliminar algunos nodos y verificar balanceo
        self.db.borrar_temperatura("05/05/2023")
        self._assert_avl_balance(self.db._Temperaturas_DB__arbol.raiz)
        self.db.borrar_temperatura("25/05/2023")
        self._assert_avl_balance(self.db._Temperaturas_DB__arbol.raiz)
        self.db.borrar_temperatura("15/05/2023") # Eliminar la raíz o un nodo con 2 hijos
        self._assert_avl_balance(self.db._Temperaturas_DB__arbol.raiz)

        self.assertEqual(self.db.cantidad_muestras(), f"Cantidad de muestras en la base de datos: {len(dates) - 3}")


    def _assert_avl_balance(self, node):
        """
        Función auxiliar recursiva para verificar que todos los nodos
        en el subárbol tienen un factor de equilibrio válido (-1, 0, 1).
        Se usa para validar el comportamiento interno del AVL.
        """
        if node is None:
            return True
        
        # Verificar que el factor de equilibrio esté en el rango permitido
        self.assertIn(node.factorEquilibrio, [-1, 0, 1], 
                      f"Nodo desbalanceado: {node.clave}, FE: {node.factorEquilibrio}")
        
        # Verificar recursivamente los hijos
        self._assert_avl_balance(node.hijoIzquierdo)
        self._assert_avl_balance(node.hijoDerecho)

        # También podríamos verificar que la altura de los subárboles difiere en no más de 1
        # Pero verificar el factorEquilibrio es generalmente suficiente si la lógica de AVL es correcta.


# Permite ejecutar los tests directamente desde la línea de comandos
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)