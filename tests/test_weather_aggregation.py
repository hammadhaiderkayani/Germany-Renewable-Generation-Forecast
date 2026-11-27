
import sys
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.features.weather_aggregation import aggregate_weather_by_region


def test_regional_aggregation_columns():
    df = pd.DataFrame({
        "Hamburg": [10, 20],
        "Bremen": [20, 30],
        "Berlin": [30, 40]
    })

    result = aggregate_weather_by_region(
        df,
        ["Hamburg", "Bremen", "Berlin"],
        "North"
    )

    expected = [
        "North_mean",
        "North_std",
        "North_min",
        "North_max"
    ]

    for column in expected:
        assert column in result.columns


def test_regional_aggregation_values():
    df = pd.DataFrame({
        "Hamburg": [10],
        "Bremen": [20],
        "Berlin": [30]
    })

    result = aggregate_weather_by_region(
        df,
        ["Hamburg", "Bremen", "Berlin"],
        "North"
    )

    assert np.isclose(result.loc[0, "North_mean"], 20)
    assert np.isclose(result.loc[0, "North_std"], 10)
    assert np.isclose(result.loc[0, "North_min"], 10)
    assert np.isclose(result.loc[0, "North_max"], 30)


def test_original_dataframe_is_preserved():
    df = pd.DataFrame({
        "Hamburg": [10],
        "Bremen": [20]
    })

    original_columns = df.columns.tolist()

    result = aggregate_weather_by_region(
        df,
        ["Hamburg", "Bremen"],
        "North"
    )

    assert df.columns.tolist() == original_columns
    assert len(result) == len(df)
