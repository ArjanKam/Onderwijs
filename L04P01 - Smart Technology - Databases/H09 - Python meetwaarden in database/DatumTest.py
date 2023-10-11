from Datum import Datum
import unittest

class DatumTest(unittest.TestCase):
    def setUp(self):
        None
    # testing __init__
    def test_constructor(self):
        self.assertEqual(Datum(1, 1, 2020).getDatum(), (1,1,2020))
    def test_constructor_Error(self):
        with self.assertRaises(ValueError):
            x = Datum(31, 2, 2020)
    # testing __lt__
    def test_less_is_true(self):
        self.assertTrue(Datum(1, 1, 2020) < Datum(1, 2, 2020))
    def test_less_is_false(self):
        self.assertFalse(Datum(1, 2, 2020) < Datum(1, 1, 2020))
    # testing __gt__
    def test_greater_is_true(self):
        self.assertTrue(Datum(29, 2, 2020) > Datum(28, 2, 2020))
    def test_greater_is_false(self):
        self.assertFalse(Datum(28, 2, 2020) > Datum(29, 2, 2020))
        
if __name__ == '__main__':
    unittest.main()

