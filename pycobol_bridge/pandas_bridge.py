import pandas as pd


def records_to_dataframe(records: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(records)
