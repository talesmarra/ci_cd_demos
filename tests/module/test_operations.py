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
    def test_operations_wrong_inputs_case(self):
        """
        Scenario: wrong input type (string)
        Expected behaviour: should raise TypeError for the following: 
        add, subtract, divide.
        """
        for operation in [add, subtract, multiply, divide]:
            with self.assertRaises(TypeError):
                operation(2, 'c')
