import pyarrow as pa


def records_to_arrow(records: list[dict]):
    return pa.Table.from_pylist(records)
