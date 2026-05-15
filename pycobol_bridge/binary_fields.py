import struct


def decode_binary_integer(data: bytes, signed=True):
    fmt = '>i' if signed else '>I'
    return struct.unpack(fmt, data)[0]
