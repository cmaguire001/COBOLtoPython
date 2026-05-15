import codecs

SUPPORTED_CODEPAGES = [
    'cp037',
    'cp500',
    'cp1140'
]


def decode_ebcdic(data: bytes, encoding: str = 'cp037') -> str:
    if encoding not in SUPPORTED_CODEPAGES:
        raise ValueError(f'Unsupported EBCDIC encoding: {encoding}')

    return codecs.decode(data, encoding)


def encode_ebcdic(text: str, encoding: str = 'cp037') -> bytes:
    if encoding not in SUPPORTED_CODEPAGES:
        raise ValueError(f'Unsupported EBCDIC encoding: {encoding}')

    return codecs.encode(text, encoding)
