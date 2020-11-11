# Saturation Mapping
ML models to determine from local well data and deep measurements (3D measurments) the saturation pattern in the inter-well area.
ML models runned on 6 synthetic cases with water saturation, porosity and electrical resistivity data. 


## Experiment results
### Baseline:
|Model                               | MSE    |
|------------------------------------|--------|
|KNeighborsRegressor                 | 0.0585 |
|KNeighborsRegressor (fine-tuned)    |        |
|RandomForestRegressor               | 0.0159 |
|RandomForestRegressor (fine-tuned)  |        |
|CatBoost                            |        |
|CatBoost (fine-tuned)               |        |
|XGBoost                             |        |
|XGBoost (fine-tuned)                |        |
|LightGBM                            |        |
|LightGBM (fine-tuned)               |        |

### Conslusion:

Even the simple regression models shows good results. However, it is possible to improve model (assumption!) using to improve model using 3D input.
Current models were implemented  using 1D inputs.
