from pycobol_bridge.copybook import CopybookParser


def test_copybook_parser():
    copybook = '''
       05 CUSTOMER-ID PIC X(10).
       05 BALANCE PIC 9(5).
    '''

    parser = CopybookParser.from_string(copybook)

    assert len(parser.fields) == 2
    assert parser.fields[0].name == 'CUSTOMER-ID'


def test_parse_line():
    copybook = '''
       05 CUSTOMER-ID PIC X(10).
       05 BALANCE PIC 9(5).
    '''

    parser = CopybookParser.from_string(copybook)

    result = parser.parse_line('123456789000500')

    assert result['CUSTOMER-ID'] == '1234567890'
    assert result['BALANCE'] == '00500'
