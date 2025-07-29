import unittest
from calculator_class import addition, subtraction, multiply, Divide  # import the class name

class TestCalculator(unittest.TestCase):

    def test_add(self): # test methods should only take self as a parameter
        calc = addition()
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-3, 13), 10)
        self.assertEqual(calc.add(0, 0), 0)

    def test_subtract(self):
        calc = subtraction()
        self.assertEqual(calc.sub(10, 5), 5)
        # self.assertEqual(calc.sub(5, 10), -5)
        # self.assertEqual(calc.sub(0, 0), 0)

    def test_multiply(self):
        calc = multiply()
        self.assertEqual(calc.mul(4, 5), 20)
        # self.assertEqual(calc.mul(0, 5), 0)
        # self.assertEqual(calc.mul(-2, 3), -6)

    def test_divide(self):
        calc = Divide()
        self.assertEqual(calc.div(10, 2), 5)
        # self.assertEqual(calc.div(-9, 3), -3)
        # self.assertAlmostEqual(calc.div(7, 2), 3.5)

    def test_divide_by_zero(self):
        calc = Divide()
        with self.assertRaises(ValueError):
            calc.div(10, 0)

# Run the tests
if __name__ == "__main__":
    unittest.main()


# to run : 
# cd .\Testing\python-pytest\  
# python -m pytest test_calculator_class.py
# python -m unittest test_calculator_class.py