import unittest  # Importing Python's built-in unit testing framework
from greeter import Greeter  # Importing the Greeter class from greeter.py

# Creating a test class that inherits from unittest.TestCase
class TestGreeter(unittest.TestCase):

    # Test method to check the output of say_hello() method
    def test_say_hello(self):
        g = Greeter("Aman")  # Creating an object of Greeter class with name "Aman"
        self.assertEqual(g.say_hello(), "Hello, Aman")  # Asserting the output matches expected greeting

# This ensures that the tests run only when the file is executed directly (not when imported)
# Entry point to run the tests
if __name__ == "__main__":
    unittest.main()


# to run: cd .\Testing\python-pytest\  //otherwise cause error file not found 
# python -m pytest test_greeter.py
# python -m unittest test_greeter.py  //based on library name