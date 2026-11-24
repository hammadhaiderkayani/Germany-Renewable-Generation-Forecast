

\# Feature Engineering



This module contains reusable feature-engineering functions for the German renewable energy generation forecasting project.



\## Modules



\### 1. `weather\_features.py`

Creates cyclical time features:

\- Hour of day (sine and cosine encoding)

\- Day of year (sine and cosine encoding)



\### 2. `weather\_transformations.py`

Transforms wind direction from degrees into sine and cosine representations to preserve its circular nature.



\### 3. `weather\_aggregation.py`

Provides regional weather aggregation functions:

\- Mean

\- Standard deviation

\- Minimum

\- Maximum



\## Purpose



Feature engineering converts raw meteorological and temporal variables into structured inputs suitable for machine-learning models.



These functions are reusable utilities. The exact features used by each trained model are documented separately in the model artifacts.



