import pandas as pd
import datetime as dt
from pathlib import Path

def ensure_today_demo(csv_in: str, csv_out: str):
    today = dt.date.today()
    df = pd.read_csv(csv_in, parse_dates=['date'])
    df['date'] = pd.to_datetime(today)
    Path(csv_out).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_out, index=False)

def load_today_matches(csv_processed: str):
    df = pd.read_csv(csv_processed, parse_dates=['date'])
    df['date'] = df['date'].dt.date
    today = dt.date.today()
    return df[df['date']==today].copy()
