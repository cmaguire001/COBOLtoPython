from dataclasses import dataclass

@dataclass
class RedefinesField:
    original: str
    alias: str


def apply_redefines(record: dict, redefines: list):
    for redefine in redefines:
        if redefine.original in record:
            record[redefine.alias] = record[redefine.original]
    return record
