import unittest

from pyadsb.algebra import Polynomial


class TestPolynomial(unittest.TestCase):

    def setUp(self):
        self.f = Polynomial([0, 1, 1])
        self.g = Polynomial([1, 0, 1, 1])

    def test_equality(self):
        self.assertEqual(self.f, Polynomial([0, 1, 1]))
        self.assertNotEqual(self.f, self.g)
        self.assertNotEqual(self.f, 'X + X^2')

    def test_reduce_coefficients_modulo_two(self):
        self.assertEqual(Polynomial([0, 1, 2, 3]), Polynomial([0, 1, 0, 1]))

    def test_trim_leading_zeroes(self):
        self.assertEqual(Polynomial([0, 1, 1, 0, 0]), Polynomial([0, 1, 1]))

    def test_add_binary_polynomials(self):
        self.assertEqual(self.f + self.g, Polynomial([1, 1, 0, 1]))

    def test_multiply_binary_polynomials(self):
        self.assertEqual(self.f * self.g, Polynomial([0, 1, 1, 1, 0, 1]))

    def test_division_with_remainder(self):
        q, r = divmod(self.g, Polynomial([1, 1]))
        self.assertEqual(q, Polynomial([0, 0, 1]))
        self.assertEqual(r, Polynomial([1]))

    def test_degree(self):
        self.assertEqual(self.f.degree, 2)
        self.assertEqual(self.g.degree, 3)

    def test_degree_extreme_cases(self):
        self.assertEqual(Polynomial([1]).degree, 0)
        self.assertEqual(Polynomial([0]).degree, -1)
