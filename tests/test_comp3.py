from decimal import Decimal
from pycobol_bridge.comp3 import decode_comp3


def test_decode_comp3_positive():
    packed = bytes([18, 52, 92])
    result = decode_comp3(packed)
    assert result == Decimal('123.45')


def test_decode_comp3_negative():
    packed = bytes([18, 52, 93])
    result = decode_comp3(packed)
    assert result == Decimal('-123.45')
