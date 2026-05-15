from dataclasses import dataclass
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class CobolField:
    name: str
    pic: str

class CopybookParser:
    def __init__(self, fields):
        self.fields = fields

    @classmethod
    def from_string(cls, text: str):
        fields = []
        pattern = r'\d+\s+([A-Z0-9-]+)\s+PIC\s+([XS9V\(\)]+)'

        for line in text.splitlines():
            match = re.search(pattern, line.strip(), re.IGNORECASE)
            if match:
                field = CobolField(match.group(1), match.group(2))
                fields.append(field)
                logger.info(f'Parsed field: {field}')

        return cls(fields)

    def parse_line(self, line: str):
        result = {}
        cursor = 0

        for field in self.fields:
            width = self._pic_width(field.pic)
            result[field.name] = line[cursor:cursor+width].strip()
            cursor += width

        return result

    def _pic_width(self, pic: str):
        match = re.search(r'\((\d+)\)', pic)
        if match:
            return int(match.group(1))
        return 1
