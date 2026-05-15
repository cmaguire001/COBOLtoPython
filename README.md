# pyCOBOL Bridge

Modern Python interoperability toolkit for COBOL data systems.

## Features
- Copybook parsing
- Fixed-width record decoding
- COMP-3 packed decimal decoding
- Typed Python models
- Structured logging
- Pytest suite

## Example
```python
from pycobol_bridge import CopybookParser

schema = CopybookParser.from_string(copybook)
record = schema.parse_line(line)
print(record)
```
