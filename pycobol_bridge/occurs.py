from dataclasses import dataclass

@dataclass
class OccursField:
    name: str
    count: int
    children: list


def expand_occurs(field):
    expanded = []
    for i in range(field.count):
        for child in field.children:
            expanded.append(f"{field.name}_{i+1}_{child.name}")
    return expanded
