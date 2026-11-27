# Germany Renewable Generation Forecasting

### Machine Learning Pipeline for Forecasting German Onshore Wind, Offshore Wind and Solar Power Generation

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-LightGBM%20%7C%20Scikit--learn-green)
![Geography](https://img.shields.io/badge/Region-Germany-orange)
![Project](https://img.shields.io/badge/Project-Research%20%26%20Development-purple)

## 1. Project Overview

This project develops a machine-learning pipeline for forecasting hourly renewable electricity generation in Germany.

The system focuses on three major renewable energy sources:

- Onshore wind generation
- Offshore wind generation
- Solar photovoltaic generation

The objective is to transform meteorological information and temporal patterns into hourly electricity generation predictions, measured in megawatts (MW).

The project combines historical generation data, weather information, feature engineering, machine-learning models, calibration and historical performance evaluation.

## 2. Forecasting Architecture

The pipeline covers three forecasting targets:

| Generation Source | Forecast Target |
|---|---|
| Onshore wind | Onshore wind generation (MW) |
| Offshore wind | Offshore wind generation (MW) |
| Solar | Solar generation (MW) |

Each technology uses its own model and source-specific feature set.

## 3. Data Sources

The project uses the following data sources:

- **SMARD:** Historical German electricity generation data.
- **Open-Meteo:** Meteorological weather data and weather forecast inputs.
- **Temporal variables:** Hour-of-day and day-of-year information.

Historical generation observations are used as model targets, while meteorological variables provide weather-related inputs.

## 4. Feature Engineering

Feature engineering transforms raw meteorological and temporal data into meaningful machine-learning features.

The pipeline includes:

- Cyclical time encoding using sine and cosine transformations.
- Wind direction encoding using sine and cosine transformations.
- Regional weather aggregation.
- Meteorological transformations.
- Wind speed, temperature, solar radiation and cloud cover features.
- Technology-specific feature selection and preparation.

Dedicated feature engineering modules are maintained in `src/features/`.

## 5. Machine Learning Models

The repository contains trained models for three renewable generation technologies:

| Target | Model Family |
|---|---|
| Onshore wind | LightGBM |
| Offshore wind | LightGBM |
| Solar | Histogram-based Gradient Boosting |

The wind forecasting pipeline also includes saved calibration artifacts.

The historical backtesting workflow evaluates the saved models without retraining or modifying them.

## 6. Historical Backtesting

A historical backtesting framework was developed to evaluate the three generation models against actual German renewable generation.

The evaluation covers 30 complete calendar months.

A detailed hourly case study was conducted for September 2025, containing 720 hourly observations.

### September 2025 Performance

| Technology | MAE (MW) | RMSE (MW) | Bias (MW) | WAPE |
|---|---:|---:|---:|---:|
| Solar | 1,483.68 | 2,517.25 | +554.52 | 16.60% |
| Onshore wind | 1,158.43 | 1,504.67 | +645.26 | 8.59% |
| Offshore wind | 416.45 | 536.49 | +85.30 | 12.46% |

**Average WAPE across the three technologies: 12.55%.**

September 2025 was selected as the featured case study because it achieved the lowest average WAPE across the three technologies among the 30 evaluated complete months. It is not intended to represent typical performance across all periods.

### Evaluation Metrics

- **MAE:** Mean Absolute Error.
- **RMSE:** Root Mean Squared Error.
- **Bias:** Average signed prediction error.
- **WAPE:** Weighted Absolute Percentage Error.

All generation errors are expressed in MW, except WAPE, which is expressed as a percentage.

Detailed results and visualisations are available in the `backtesting/` directory.

## 7. Important Evaluation Limitations

The historical backtesting exercise uses archived historical weather data rather than genuine historical day-ahead weather forecast vintages.

Therefore, these results evaluate model performance using archived weather information but do not establish strict operational day-ahead forecasting performance or prove that every input was available before the market gate closure.

A separate evaluation using historical weather forecast vintages would be required to establish strict point-in-time operational performance.

## 8. Repository Structure

```text
Germany-Renewable-Generation-Forecast/
│
├── backtesting/
│   ├── results/
│   ├── plots/
│   ├── 01_Historical_Backtesting.ipynb
│   └── README.md
│
├── models/
│   ├── Shared/
│   ├── Solar/
│   └── Wind/
│
├── notebooks/
│   └── 01_Data_Inspection.ipynb
│
├── src/
│   ├── data/
│   │   └── data_validation.py
│   │
│   ├── evaluation/
│   │   └── forecast_metrics.py
│   │
│   └── features/
│       ├── README.md
│       ├── weather_aggregation.py
│       ├── weather_features.py
│       └── weather_transformations.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 9. Installation

Clone the repository:

```bash
git clone https://github.com/hammadhaiderkayani/Germany-Renewable-Generation-Forecast.git
```

Navigate into the project:

```bash
cd Germany-Renewable-Generation-Forecast
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 10. Project Scope

This repository is organised as a research and development project focused on renewable electricity generation forecasting in Germany.

It brings together:

- Historical electricity generation data.
- Meteorological inputs.
- Feature engineering and weather transformations.
- Technology-specific machine-learning models.
- Wind model calibration.
- Historical backtesting and performance evaluation.
- Reproducible evaluation outputs and visualisations.

## Author

**Hammad Haider Kayani**

GitHub: [hammadhaiderkayani](https://github.com/hammadhaiderkayani)