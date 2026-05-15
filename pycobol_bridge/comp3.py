from decimal import Decimal


def decode_comp3(data: bytes, decimals: int = 2) -> Decimal:
    digits = ''

    for byte in data[:-1]:
        digits += f'{byte >> 4}{byte & 0x0F}'

    last = data[-1]
    digits += str(last >> 4)

    sign = -1 if (last & 0x0F) == 0x0D else 1

    value = Decimal(digits) / (10 ** decimals)
    return value * sign
