import unittest
from App import calculadora

class teste_SomaNumerica(unittest.TestCase):

    origin = calculadora()

    def test_soma(self):
        self.assertEquals(self.origin.Soma(10,10), 20)
        self.assertEquals(self.origin.Soma(16,-6), 10)
        self.assertEquals(self.origin.Soma(0,-1), -1)

    def test_sub(self):
        self.assertEquals(self.origin.Subtracao(25,50), -25)
        self.assertEquals(self.origin.Subtracao(-5,-10), 5)

    def test_div(self):
        self.assertEquals(self.origin.Divisao(10,2), 5)
        self.assertEquals(self.origin.Divisao(4,1), 4)
        self.assertEquals(self.origin.Divisao(1,5), 0.2)
        #self.assertEquals(self.origin.Divisao(20,0), error)

if __name__ == "__main__":
    unittest.main()
