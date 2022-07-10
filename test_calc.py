import unittest
from unittest.mock import patch

import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 15), 25)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 15), -5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 15), 150)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 15), 10 / 15)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        self.assertRaises(ZeroDivisionError, calc.divide, 100, 0)

        # Invalid experiment case
        # self.assertEqual(calc.add(10, 15), 24)

    def test_get_page(self):
        with patch("calc.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success!"

            url = "https://translate.google.com"
            calc.get_page(url)
            mocked_get.assert_called_with(url)


if __name__ == "__main__":
    unittest.main()
