import re

from pyadsb.exceptions import HexConversionError


def hex_to_bin(hex: str) -> str:
    if not re.match(r'[0-9a-f]+$', hex):
        raise HexConversionError(f'Not a valid hexadecimal number: {hex}')
    return '{:b}'.format(int(hex, 16))
