
import numpy as np


def add_wind_direction_features(df, direction_columns):
    """
    Convert wind direction from degrees into sine and cosine features.

    This avoids treating 359° and 1° as very different directions.
    """
    df = df.copy()

    for column in direction_columns:
        radians = np.deg2rad(df[column])

        df[column.replace("wind_direction", "wind_direction_sin")] = (
            np.sin(radians)
        )

        df[column.replace("wind_direction", "wind_direction_cos")] = (
            np.cos(radians)
        )

    return df
