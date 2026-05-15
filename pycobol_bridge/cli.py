import argparse
from pycobol_bridge.copybook import CopybookParser


def main():
    parser = argparse.ArgumentParser(description='pyCOBOL Bridge CLI')
    parser.add_argument('--copybook', required=True)
    parser.add_argument('--data', required=True)

    args = parser.parse_args()

    with open(args.copybook) as f:
        schema = CopybookParser.from_string(f.read())

    with open(args.data) as f:
        for line in f:
            print(schema.parse_line(line))


if __name__ == '__main__':
    main()
