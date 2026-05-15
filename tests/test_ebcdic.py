from pycobol_bridge.ebcdic import encode_ebcdic, decode_ebcdic


def test_ebcdic_roundtrip():
    original = 'HELLO'
    encoded = encode_ebcdic(original)
    decoded = decode_ebcdic(encoded)

    assert decoded == original
