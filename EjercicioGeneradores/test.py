# test_numeros.py

import unittest
from principal import obtener_turno

class TestTurnos(unittest.TestCase):

    def test_turno_optica(self):
        self.assertEqual(obtener_turno("Óptica"), "Su turno es: O-1. Espere a ser atendido.")
        self.assertEqual(obtener_turno("Óptica"), "Su turno es: O-2. Espere a ser atendido.")

    def test_turno_farmacia(self):
        self.assertEqual(obtener_turno("Farmacia"), "Su turno es: F-1. Espere a ser atendido.")
        self.assertEqual(obtener_turno("Farmacia"), "Su turno es: F-2. Espere a ser atendido.")

    def test_turno_cosmetica(self):
        self.assertEqual(obtener_turno("Cosmética"), "Su turno es: C-1. Espere a ser atendido.")
        self.assertEqual(obtener_turno("Cosmética"), "Su turno es: C-2. Espere a ser atendido.")

    def test_area_no_valida(self):
        with self.assertRaises(ValueError):
            obtener_turno("InvalidArea")

if __name__ == "__main__":
    unittest.main()