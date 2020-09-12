import unittest
import funcs


class TestPrimeNum(unittest.TestCase):
    def test_prime_4(self):
        is_prime = funcs.is_prime(4)
        self.assertEqual(is_prime, False)

    def test_prime_5(self):
        is_prime = funcs.is_prime(5)
        self.assertEqual(is_prime, True)

    def test_prime_10000(self):
        is_prime = funcs.is_prime(10000)
        self.assertEqual(is_prime, False)


class TestAbs(unittest.TestCase):
    def test_abs_5(self):
        absolute = funcs.get_absolute_value(5)
        self.assertEqual(absolute, 5)

    def test_abs_neg5(self):
        absolute = funcs.get_absolute_value(-5)
        self.assertEqual(absolute, 5)

    def test_abs_0(self):
        absolute = funcs.get_absolute_value(0)
        self.assertEqual(absolute, 0)


unittest.main()
