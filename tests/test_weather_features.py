
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.features.weather_features import add_cyclical_time_features


def test_cyclical_time_features_columns():
    df = pd.DataFrame({
        "time": pd.to_datetime([
            "2025-01-01 00:00:00",
            "2025-01-01 06:00:00",
            "2025-01-01 12:00:00",
            "2025-01-01 18:00:00"
        ])
    })

    result = add_cyclical_time_features(df)

    expected = [
        "hour_sin",
        "hour_cos",
        "day_of_year_sin",
        "day_of_year_cos"
    ]

    for column in expected:
        assert column in result.columns


def test_cyclical_time_features_values():
    df = pd.DataFrame({
        "time": pd.to_datetime([
            "2025-01-01 00:00:00",
            "2025-01-01 06:00:00",
            "2025-01-01 12:00:00",
            "2025-01-01 18:00:00"
        ])
    })

    result = add_cyclical_time_features(df)

    assert np.isclose(result.loc[0, "hour_sin"], 0)
    assert np.isclose(result.loc[0, "hour_cos"], 1)

    assert np.isclose(result.loc[1, "hour_sin"], 1)
    assert np.isclose(result.loc[1, "hour_cos"], 0)


def test_original_dataframe_is_preserved():
    df = pd.DataFrame({
        "time": pd.to_datetime(["2025-01-01 00:00:00"])
    })

    original_columns = df.columns.tolist()

    result = add_cyclical_time_features(df)

    assert df.columns.tolist() == original_columns
    assert len(result) == len(df)
