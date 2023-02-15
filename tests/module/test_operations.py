import unittest
from module.operations import add, subtract, multiply, divide

class TestOperations(unittest.TestCase):
    """
    Test the operations module
    """
    def test_operations_nominal_case(self):
        """
            Tests nominal case for operations.
        """
        setup = [(2, 3, add ,5), (2, 3, subtract, -1), (2, 3, multiply, 6), (3, 2, divide, 1.5)]
        for num1, num2, operation, result in setup:
            self.assertEqual(operation(num1, num2), result)