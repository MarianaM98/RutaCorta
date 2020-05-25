from FuncionesGrafo import *
import networkx as nx


IngresarGrafo()

import unittest

class TestSFunciones(unittest.TestCase):

    def test_RutaCorta(self):
    	r,d=RutaCorta('u','v',g)
        self.assertEqual(d, 5)

if __name__ == '__main__':
    unittest.main()