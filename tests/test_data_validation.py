import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.data.data_validation import validate_dataset


def test_dataset_summary():
    df = pd.DataFrame({
        "time": pd.to_datetime([
            "2025-01-01 00:00:00",
            "2025-01-01 01:00:00",
            "2025-01-01 02:00:00"
        ]),
        "generation_mw": [100, 200, 300]
    })

    result = validate_dataset(
        df,
        required_columns=["time", "generation_mw"]
    )

    assert result["rows"] == 3
    assert result["columns"] == 2
    assert result["missing_values"] == 0
    assert result["duplicate_timestamps"] == 0


def test_missing_values_are_counted():
    df = pd.DataFrame({
        "time": pd.to_datetime([
            "2025-01-01 00:00:00",
            "2025-01-01 01:00:00"
        ]),
        "generation_mw": [100, None]
    })

    result = validate_dataset(
        df,
        required_columns=["time", "generation_mw"]
    )

    assert result["missing_values"] == 1


def test_duplicate_timestamps_are_detected():
    df = pd.DataFrame({
        "time": pd.to_datetime([
            "2025-01-01 00:00:00",
            "2025-01-01 00:00:00",
            "2025-01-01 02:00:00"
        ]),
        "generation_mw": [100, 200, 300]
    })

    result = validate_dataset(
        df,
        required_columns=["time", "generation_mw"]
    )

    assert result["duplicate_timestamps"] == 1


def test_missing_required_column_raises_error():
    df = pd.DataFrame({
        "time": pd.to_datetime(["2025-01-01 00:00:00"])
    })

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_dataset(
            df,
            required_columns=["time", "generation_mw"]
        )


def test_missing_timestamp_column_raises_error():
    df = pd.DataFrame({
        "generation_mw": [100]
    })

    with pytest.raises(ValueError, match="Timestamp column"):
        validate_dataset(
            df,
            required_columns=["generation_mw"]
        )
