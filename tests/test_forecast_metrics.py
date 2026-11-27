import sys
from pathlib import Path

import numpy as np
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.forecast_metrics import evaluate_forecast


def test_forecast_metrics_are_returned():
    actual = np.array([100, 200, 300, 400])
    predicted = np.array([110, 190, 310, 390])

    result = evaluate_forecast(actual, predicted)

    expected_metrics = [
        "MAE_MW",
        "RMSE_MW",
        "R2",
        "Bias_MW"
    ]

    for metric in expected_metrics:
        assert metric in result


def test_mae_calculation():
    actual = np.array([100, 200, 300, 400])
    predicted = np.array([110, 190, 310, 390])

    result = evaluate_forecast(actual, predicted)

    assert result["MAE_MW"] == pytest.approx(10)


def test_rmse_calculation():
    actual = np.array([100, 200, 300, 400])
    predicted = np.array([110, 190, 310, 390])

    result = evaluate_forecast(actual, predicted)

    assert result["RMSE_MW"] == pytest.approx(10)


def test_r2_calculation():
    actual = np.array([100, 200, 300, 400])
    predicted = np.array([110, 190, 310, 390])

    result = evaluate_forecast(actual, predicted)

    assert result["R2"] == pytest.approx(0.992)


def test_bias_calculation():
    actual = np.array([100, 200, 300, 400])
    predicted = np.array([110, 190, 310, 390])

    result = evaluate_forecast(actual, predicted)

    assert result["Bias_MW"] == pytest.approx(0)
