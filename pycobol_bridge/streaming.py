from pycobol_bridge.copybook import CopybookParser


def stream_parse(file_path, parser: CopybookParser):
    with open(file_path) as f:
        for line in f:
            yield parser.parse_line(line)
