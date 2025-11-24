import unittest
from operaciones import *

class TestDePruebas(unittest.TestCase):

    def test_sumar(self):
        #self.assertEqual
        self.assertRaises(ZeroDivisionError)
        self.assertEqual(sumar(2,3), 5)