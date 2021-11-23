#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import factorial

class TestFactorialInvalid(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to get factorial of an invalid number
        """
        data = -2
        result = factorial(data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
