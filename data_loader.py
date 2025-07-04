import pandas as pd

def load_health_data(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df
