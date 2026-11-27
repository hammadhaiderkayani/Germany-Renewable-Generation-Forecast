# Automated Tests

This directory contains automated unit tests for the project's data validation, feature engineering, weather transformations, and forecast evaluation modules.

## Test Coverage

| Test File | Description |
|---|---|
| test_data_validation.py | Tests dataset validation, missing values, and duplicate timestamps |
| test_forecast_metrics.py | Tests MAE, RMSE, R2, and forecast bias calculations |
| test_weather_aggregation.py | Tests regional weather aggregation |
| test_weather_features.py | Tests cyclical time feature engineering |
| test_weather_transformations.py | Tests wind direction sine and cosine transformations |

## Running the Tests

Install project dependencies:

    pip install -r requirements.txt

Install development dependencies:

    pip install -r requirements-dev.txt

Run the complete test suite from the project root:

    python -m pytest tests/ -v

## Latest Test Results

- Total tests: 19
- Passed: 19
- Failed: 0
- Status: All tests passed

## Purpose

These tests verify the correctness and reliability of individual project components. They do not retrain or modify the saved forecasting models.
