# Saturation Mapping
ML models to determine from local well data and deep measurements (3D measurments) the saturation pattern in the inter-well area.
ML models runned on 6 synthetic cases with water saturation, porosity and electrical resistivity data. 

## Problem
 - Understanding reservoir fluid flow is a major challenge for oil and gas companies to optimize sweep efficiency and improve recovery.  
 - Understanding of the saturation pattern is crucial to optimizing water injection, as well as the drilling of new wells. 
 - The challenge is to determine from local well data and deep measurements the saturation pattern in the interwell area. 
 
## Solution
Solution is implemented in Python 3.8.  
**Input**: Resistivity, Porosity.  
**Output**: Water saturation map – export into text format.  

## Experiment results
### [Baseline 1D](https://github.com/Xrenya/SaturationMapping/blob/main/Baseline_1D.ipynb):
|Model                               | MSE    |
|------------------------------------|--------|
|KNeighborsRegressor                 | 0.0585 |
|KNeighborsRegressor (fine-tuned)    | NA     |
|[RandomForestRegressor](https://github.com/Xrenya/SaturationMapping/tree/main/RandomForestRegressor)               |**0.0157**|
|RandomForestRegressor (fine-tuned)  | NA     |
|CatBoost                            | 0.0682 |
|CatBoost (fine-tuned)               | NA     |
|XGBoost                             | 0.0214 |
|XGBoost (fine-tuned)                | NA     |
|LightGBM                            | 0.0581 |
|LightGBM (fine-tuned)               | NA     |

### [Baseline 2D]
|Model                               | MSE    |
|------------------------------------|--------|
|                                    | NA     |

### [Baseline 3D]
|Model                               | MSE    |
|------------------------------------|--------|
|                                    | NA     |

### Pipeline:
 Data &rarr; Preprocessing: Standart Scaler* &rarr; Model
 
 *<sub>(StandardScaler standardizes a feature by subtracting the mean and then scaling to unit variance. Unit variance means dividing all the values by the standard deviation)</sub>

### Conslusion:

Even the simple RandomForestRegressor model shows good results.
