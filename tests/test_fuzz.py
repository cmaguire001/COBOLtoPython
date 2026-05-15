import random
import string
from pycobol_bridge.copybook import CopybookParser


def random_record(length=20):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def test_random_record_parsing():
    copybook = '05 FIELD PIC X(20).'
    parser = CopybookParser.from_string(copybook)

    for _ in range(100):
        record = random_record()
        parsed = parser.parse_line(record)
        assert parsed['FIELD'] == record
