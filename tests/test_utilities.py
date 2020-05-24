import unittest

from pyadsb.exceptions import HexConversionError

from pyadsb.utilities import hex_to_bin


class TestHexUtilities(unittest.TestCase):

    def test_hex_to_bin(self):
        self.assertEqual(hex_to_bin(hex='0'), '0')
        self.assertEqual(hex_to_bin(hex='1'), '1')
        self.assertEqual(hex_to_bin(hex='a'), '1010')
        self.assertEqual(hex_to_bin(hex='1a'), '11010')
        self.assertEqual(hex_to_bin(hex='1d7'), '111010111')

    def test_non_hex_input_raises_exception(self):
        with self.assertRaises(HexConversionError):
            hex_to_bin(hex='1gaf7')
