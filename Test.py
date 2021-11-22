#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation, factorial

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [23, 32]
        result = summation(data)
        self.assertEqual(result, 55)

class TestFactorialValid(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to get factorial of a valid number
        """
        data = 4
        result = factorial(data)
        self.assertEqual(result, 24)
     
class TestFactorialInvalid(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to get factorial of an invalid number
        """
        data = -2
        result = factorial(data)
        self.assertEqual(result, null)

if __name__ == '__main__':
    unittest.main()
