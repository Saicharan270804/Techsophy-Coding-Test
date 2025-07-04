# detection.py
import pandas as pd

def detect_outbreaks(df, window_size=7, z_thresh=2.0):
    """
    Detect anomalies in health data using rolling average and z-score.
    Returns rows where z-score > threshold.
    """
    df = df.copy()
    df['rolling_mean'] = df.groupby('region')['cases'].transform(lambda x: x.rolling(window=window_size, min_periods=1).mean())
    df['rolling_std'] = df.groupby('region')['cases'].transform(lambda x: x.rolling(window=window_size, min_periods=1).std())
    
    df['z_score'] = (df['cases'] - df['rolling_mean']) / (df['rolling_std'] + 1e-5)
    outbreak_df = df[df['z_score'] > z_thresh].reset_index(drop=True)

    return outbreak_df
