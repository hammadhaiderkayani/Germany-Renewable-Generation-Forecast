
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_forecast(actual, predicted):
    """
    Calculate standard regression metrics for generation forecasts.

    Returns MAE, RMSE, R² and mean bias in MW.
    """
    actual = np.asarray(actual)
    predicted = np.asarray(predicted)

    return {
        "MAE_MW": mean_absolute_error(actual, predicted),
        "RMSE_MW": np.sqrt(mean_squared_error(actual, predicted)),
        "R2": r2_score(actual, predicted),
        "Bias_MW": np.mean(predicted - actual),
    }
