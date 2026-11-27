import sys
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.features.weather_transformations import add_wind_direction_features


def test_wind_direction_feature_columns():
    df = pd.DataFrame({
        "wind_direction_100m": [0, 90, 180, 270]
    })

    result = add_wind_direction_features(
        df, ["wind_direction_100m"]
    )

    assert "wind_direction_sin_100m" in result.columns
    assert "wind_direction_cos_100m" in result.columns


def test_wind_direction_feature_values():
    df = pd.DataFrame({
        "wind_direction_100m": [0, 90, 180, 270]
    })

    result = add_wind_direction_features(
        df, ["wind_direction_100m"]
    )

    expected_sin = [0, 1, 0, -1]
    expected_cos = [1, 0, -1, 0]

    np.testing.assert_allclose(
        result["wind_direction_sin_100m"],
        expected_sin,
        atol=1e-10
    )

    np.testing.assert_allclose(
        result["wind_direction_cos_100m"],
        expected_cos,
        atol=1e-10
    )


def test_original_dataframe_is_preserved():
    df = pd.DataFrame({
        "wind_direction_100m": [0, 90, 180, 270]
    })

    original_columns = df.columns.tolist()

    result = add_wind_direction_features(
        df, ["wind_direction_100m"]
    )

    assert df.columns.tolist() == original_columns
    assert len(result) == len(df)
