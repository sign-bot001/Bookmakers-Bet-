import pandas as pd

def load_demo_matches(csv_path: str):
    return pd.read_csv(csv_path, parse_dates=['date'])
