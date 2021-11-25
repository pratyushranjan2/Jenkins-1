#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import factorial

class TestFactorialValid(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to get factorial of a valid number
        """
        data = 4
        result = factorial(data)
        self.assertEqual(result, 2)
     
if __name__ == '__main__':
    unittest.main()
