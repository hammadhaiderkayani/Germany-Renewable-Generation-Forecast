
import numpy as np
import pandas as pd


def add_cyclical_time_features(df):
    """
    Add cyclical hour-of-day and day-of-year features.

    Cyclical encoding represents time as a continuous cycle,
    so that adjacent periods remain close to each other.
    """
    df = df.copy()

    hour = df["time"].dt.hour
    day_of_year = df["time"].dt.dayofyear

    df["hour_sin"] = np.sin(2 * np.pi * hour / 24)
    df["hour_cos"] = np.cos(2 * np.pi * hour / 24)

    df["day_of_year_sin"] = np.sin(2 * np.pi * day_of_year / 365.25)
    df["day_of_year_cos"] = np.cos(2 * np.pi * day_of_year / 365.25)

    return df
