import unittest
from App import calculadora

class teste_SomaNumerica(unittest.TestCase):

    origin = calculadora()

    def test_soma(self):
        self.assertEqual(self.origin.Soma(10,10), 20)
        self.assertEqual(self.origin.Soma(16,-6), 10)
        self.assertEqual(self.origin.Soma(0,-1), -1)

    def test_sub(self):
        self.assertEqual(self.origin.Subtracao(25,50), -25)
        self.assertEqual(self.origin.Subtracao(-5,-10), 5)

    def test_div(self):
        self.assertEqual(self.origin.Divisao(10,2), 5)
        self.assertEqual(self.origin.Divisao(4,1), 4)
        self.assertEqual(self.origin.Divisao(1,5), 0.2)
        #self.assertEqual(self.origin.Divisao(20,0), error)
        with self.assertRaises(ZeroDivisionError):
            self.origin.Divisao(20, 0)

    def test_mul(self):
        self.assertEqual(self.origin.Multiplicacao(10,10), 100)
        self.assertEqual(self.origin.Multiplicacao(4,1), 4)
        self.assertEqual(self.origin.Multiplicacao(1,5), 5)
        self.assertEqual(self.origin.Multiplicacao(20,0), 0)

if __name__ == "__main__":
    unittest.main()
