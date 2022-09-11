import unittest

from main import add


class TestMain(unittest.TestCase):
    """
    Recommendations:
     - Name your tests correctly and also document them using docstring - this really helps to know when
     a test should be kept, removed or replaced.
    """
    def test_invalid_type(self):
        """
        When passing invalid type (str) we expect an exception to be raised
        """
        with self.assertRaises(TypeError):
            add('string', 2)

    def test_nominal_case(self):
        """
        Nominal case, summing up two numbers.
        """
        self.assertEqual(add(1, 2), 3)

