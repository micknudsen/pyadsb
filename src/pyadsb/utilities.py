import re

from pyadsb.exceptions import HexConversionError


def hex_to_bin(hex: str) -> str:
    if not re.match(r'[0-9A-Fa-f]{28}$', hex):
        raise HexConversionError
    return '{:112b}'.format(int(hex, 16))
