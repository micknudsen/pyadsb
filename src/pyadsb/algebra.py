class BinaryPolynomial:

    def __init__(self, coefficients) -> None:
        reduced_coefficients = [coefficient % 2 for coefficient in coefficients]
        while reduced_coefficients and reduced_coefficients[-1] == 0:
            reduced_coefficients.pop(-1)
        self._coefficients = reduced_coefficients

    def __eq__(self, other: 'BinaryPolynomial') -> bool:
        return self._coefficients == other._coefficients
