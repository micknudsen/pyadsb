import unittest

from pyadsb.exceptions import HexConversionError
from pyadsb.utilities import hex_to_bin


class TestHexUtilities(unittest.TestCase):

    def test_hex_to_bin(self):
        self.assertEqual(hex_to_bin(hex='a8000d8e80361525c0048d28ee82'),
                         '1010100000000000000011011000111010000000001101100001010100100101110000000000010010001101001010001110111010000010')

    def test_too_short_hex_raises_exception(self):
        with self.assertRaises(HexConversionError):
            hex_to_bin(hex='5d5110dd258e3a')

    def test_too_long_hex_raises_exception(self):
        with self.assertRaises(HexConversionError):
            hex_to_bin(hex='8d5110dd5045f506cdeb83730a99cfda2')

    def test_non_hex_input_raises_exception(self):
        with self.assertRaises(HexConversionError):
            hex_to_bin(hex='ewqj5idv91hgko3afsn64z0ypcml')
