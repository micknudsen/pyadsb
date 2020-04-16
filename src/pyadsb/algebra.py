from itertools import zip_longest
from typing import List


class BinaryPolynomial:

    def __init__(self, coefficients: List[int]) -> None:
        reduced_coefficients = [coefficient % 2 for coefficient in coefficients]
        while reduced_coefficients and reduced_coefficients[-1] == 0:
            reduced_coefficients.pop(-1)
        self._coefficients = reduced_coefficients

    @property
    def degree(self) -> int:
        return len(self._coefficients) - 1

    def __eq__(self, other: 'BinaryPolynomial') -> bool:
        return self._coefficients == other._coefficients

    def __add__(self, other: 'BinaryPolynomial') -> 'BinaryPolynomial':
        return BinaryPolynomial(coefficients=[x + y for x, y in zip_longest(self._coefficients, other._coefficients, fillvalue=0)])

    def __sub__(self, other: 'BinaryPolynomial') -> 'BinaryPolynomial':
        return self + other

    def __mul__(self, other: 'BinaryPolynomial') -> 'BinaryPolynomial':
        product = [0] * (self.degree + other.degree + 1)
        for i, x in enumerate(self._coefficients):
            for j, y in enumerate(other._coefficients):
                product[i + j] += x * y
        return BinaryPolynomial(coefficients=product)
