import unittest
import functions as f


class MyTest(unittest.TestCase):
    def test_suma(self):

        self.assertEqual(f.sumar(1, 1), 2)

        self.assertNotEqual(f.sumar(1, 1), 1)

        with self.assertRaises(TypeError): 
            f.sumar(1,'a')


    def test_resta(self):
        
        self.assertEqual(f.restar(20, 10), 10)

        self.assertNotEqual(f.restar(10, 10), -10)

        with self.assertRaises(TypeError):
            f.restar(1,'b')


    def test_divicion(self):

        self.assertEqual(f.dividir(20, 10), 2)

        with self.assertRaises(ZeroDivisionError):
            f.dividir(1,0)

        with self.assertRaises(TypeError):
            f.dividir(1,'c')


    def test_multiplicacion(self):

        self.assertEqual(f.multiplicar(20, 10), 200)

        self.assertNotEqual(f.multiplicar(1000, 10), 10)

        with self.assertRaises(TypeError):
            f.multiplicar(10,20,30)


if __name__ == '__main__':
    unittest.main()
