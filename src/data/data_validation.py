
import pandas as pd


def validate_dataset(df, required_columns, timestamp_column="time"):
    """
    Check required columns, missing values, and duplicate timestamps.
    Returns a summary of the dataset's quality.
    """
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if timestamp_column not in df.columns:
        raise ValueError(
            f"Timestamp column '{timestamp_column}' not found."
        )

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_timestamps": int(
            df[timestamp_column].duplicated().sum()
        ),
        "start_time": df[timestamp_column].min(),
        "end_time": df[timestamp_column].max(),
    }
