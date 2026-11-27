# Historical Backtesting — Germany Renewable Generation Forecast

## 1. Overview

This directory contains the historical backtesting framework and evaluation results for the Germany Renewable Generation Forecast project.

The objective is to evaluate the performance of three machine learning models:

- Solar photovoltaic generation
- Onshore wind generation
- Offshore wind generation

The evaluation compares model predictions against historical actual generation data at hourly resolution.

## 2. Models Evaluated

The backtesting process uses the previously trained and saved models:

| Technology | Model |
|---|---|
| Solar | HistGradientBoostingRegressor |
| Onshore wind | Saved LightGBM model |
| Offshore wind | Saved LightGBM model |

The existing saved wind calibration models were also applied to the raw wind predictions.

**Important:** The backtesting process evaluates existing saved models. It does not retrain or modify them.

## 3. Evaluation Period

The historical evaluation covers 30 complete calendar months.

- Monthly results are available in `results/monthly_backtest_metrics.csv`.
- September 2025 is presented as a detailed hourly case study.
- The September case study contains 720 hourly observations.

September 2025 was selected because it achieved the lowest average WAPE across the three technologies among the 30 evaluated complete months. It is a selected case study, not a claim of typical performance.

## 4. September 2025 Results

| Technology | MAE (MW) | RMSE (MW) | Bias (MW) | WAPE |
|---|---:|---:|---:|---:|
| Solar | 1,483.68 | 2,517.25 | +554.52 | 16.60% |
| Onshore wind | 1,158.43 | 1,504.67 | +645.26 | 8.59% |
| Offshore wind | 416.45 | 536.49 | +85.30 | 12.46% |

Average WAPE across the three technologies: **12.55%**.

Positive bias indicates that predictions were higher than actual generation on average.

## 5. Evaluation Metrics

Four metrics are used:

- **MAE (Mean Absolute Error):** Average absolute difference between predicted and actual generation, measured in MW.
- **RMSE (Root Mean Squared Error):** Error metric that penalises larger prediction errors more strongly.
- **Bias:** Average signed prediction error (predicted minus actual). Positive values indicate overprediction.
- **WAPE (Weighted Absolute Percentage Error):** Total absolute error divided by total actual generation, expressed as a percentage.

## 6. Visualisations

The `plots/` directory contains:

1. `actual_vs_predicted_september_2025.png` — Hourly comparison of actual and predicted generation.
2. `error_distribution_september_2025.png` — Distribution of hourly prediction errors for each technology.

## 7. Exported Results

The `results/` directory contains:

| File | Description |
|---|---|
| `monthly_backtest_metrics.csv` | Complete monthly evaluation results for 30 months |
| `backtest_september_2025.csv` | Hourly actual values, predictions and errors for September 2025 |
| `september_2025_metrics.csv` | Summary evaluation metrics for September 2025 |

All monthly numerical results are retained to support transparent evaluation.

## 8. Methodology and Data Alignment

The evaluation combines historical German electricity generation data with archived historical weather data.

Before predictions were generated:

- Historical timestamps were aligned.
- Complete evaluation periods were identified.
- Model feature compatibility was checked.
- The original saved feature columns and their ordering were preserved.
- Existing saved models and wind calibration objects were loaded for inference.

The evaluation was performed at hourly resolution.

## 9. Important Limitations

This backtesting exercise uses archived historical weather data rather than genuine historical day-ahead weather forecast vintages.

Consequently:

- It evaluates model performance using archived weather information.
- It does not establish that all weather inputs would have been available before the day-ahead market gate closure.
- It should not be interpreted as a fully operational day-ahead forecasting validation.
- A separate evaluation using historical weather forecast vintages would be required to establish strict point-in-time operational performance.

The September 2025 results are a selected case study and should not be interpreted as representative of every month or every weather condition.

## 10. Reproducibility

The notebook `01_Historical_Backtesting.ipynb` documents the historical evaluation workflow.

The saved models, feature definitions, calibration objects, input datasets and exported results are maintained separately within the main project structure.

---

**Project:** Germany Renewable Generation Forecast  
**Evaluation:** Historical hourly backtesting  
**Technologies:** Solar, Onshore Wind and Offshore Wind