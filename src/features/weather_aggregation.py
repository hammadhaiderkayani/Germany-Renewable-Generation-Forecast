
import pandas as pd


def aggregate_weather_by_region(df, location_columns, region_name):
    """
    Calculate hourly regional averages from multiple weather locations.

    Parameters
    ----------
    df : pandas.DataFrame
        Weather dataset.
    location_columns : list
        Weather columns belonging to the selected region.
    region_name : str
        Name used for the resulting regional feature.
    """
    df = df.copy()

    df[f"{region_name}_mean"] = df[location_columns].mean(axis=1)
    df[f"{region_name}_std"] = df[location_columns].std(axis=1)
    df[f"{region_name}_min"] = df[location_columns].min(axis=1)
    df[f"{region_name}_max"] = df[location_columns].max(axis=1)

    return df
