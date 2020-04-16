import unittest

from pyadsb.algebra import BinaryPolynomial


class TestBinaryPolynomial(unittest.TestCase):

    def setUp(self):
        self.f = BinaryPolynomial(coefficients=[0, 1, 1])
        self.g = BinaryPolynomial(coefficients=[1, 0, 1, 1])

    def test_reduce_coefficients_modulo_two(self):
        self.assertEqual(BinaryPolynomial(coefficients=[0, 1, 2, 3]),
                         BinaryPolynomial(coefficients=[0, 1, 0, 1]))

    def test_trim_leading_zeroes(self):
        self.assertEqual(BinaryPolynomial(coefficients=[0, 1, 1, 0, 0]),
                         BinaryPolynomial(coefficients=[0, 1, 1]))

    def test_add_binary_polynomials(self):
        self.assertEqual(self.f + self.g, BinaryPolynomial(coefficients=[1, 1, 0, 1]))

    def test_subtract_binary_polynomials(self):
        self.assertEqual(self.f - self.g, BinaryPolynomial(coefficients=[1, 1, 0, 1]))

    def test_multiply_binary_polynomials(self):
        self.assertEqual(self.f * self.g, BinaryPolynomial(coefficients=[0, 1, 1, 1, 0, 1]))

    def test_division_with_remainder(self):
        q, r = divmod(self.f, BinaryPolynomial(coefficients=[1, 1]))
        self.assertEqual(q, BinaryPolynomial(coefficients=[0, 0, 1]))
        self.assertEqual(r, BinaryPolynomial(coefficients=[1]))

    def test_degree(self):
        self.assertEqual(self.f.degree, 2)
        self.assertEqual(self.g.degree, 3)
