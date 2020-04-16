from itertools import zip_longest
from typing import List, Tuple


class Polynomial:

    def __init__(self, coefficients: List[int]) -> None:
        reduced_coefficients = [coefficient % 2 for coefficient in coefficients]
        while reduced_coefficients and reduced_coefficients[-1] == 0:
            reduced_coefficients.pop(-1)
        self._coefficients = reduced_coefficients

    @property
    def degree(self) -> int:
        return len(self._coefficients) - 1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Polynomial):
            return NotImplemented
        return self._coefficients == other._coefficients

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        return Polynomial([x + y for x, y in zip_longest(self._coefficients, other._coefficients, fillvalue=0)])

    def __sub__(self, other: 'Polynomial') -> 'Polynomial':
        return self + other

    def __mul__(self, other: 'Polynomial') -> 'Polynomial':
        coefficients = [0] * (self.degree + other.degree + 1)
        for i, x in enumerate(self._coefficients):
            for j, y in enumerate(other._coefficients):
                coefficients[i + j] += x * y
        return Polynomial(coefficients)

    def __divmod__(self, other: 'Polynomial') -> Tuple['Polynomial', 'Polynomial']:
        zero = Polynomial([0])
        q, r = zero, self
        while r != zero and r.degree >= other.degree:
            t = Polynomial([0] * (r.degree - other.degree) + [1])
            q, r = q + t, r - (t * other)
        return q, r
