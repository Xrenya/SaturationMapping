# Saturation Mapping
ML models to determine from local well data and deep measurements (3D measurments) the saturation pattern in the inter-well area.
ML models runned on 6 synthetic cases with water saturation, porosity and electrical resistivity data. 

# Problem
 - Understanding reservoir fluid flow is a major challenge for oil and gas companies to optimize sweep efficiency and improve recovery.  
 - Understanding of the saturation pattern is crucial to optimizing water injection, as well as the drilling of new wells. 
 - The challenge is to determine from local well data and deep measurements the saturation pattern in the interwell area. 
 
# Solution
Solution is implemented in Python.  
Input: Resistivity, Porosity.  
Output: Water saturation map – export into text format.  

## Experiment results
### Baseline 1D:
|Model                               | MSE    |
|------------------------------------|--------|
|KNeighborsRegressor                 | 0.0585 |
|KNeighborsRegressor (fine-tuned)    | NA     |
|RandomForestRegressor               |**0.0159**|
|RandomForestRegressor (fine-tuned)  | NA     |
|CatBoost                            | NA     |
|CatBoost (fine-tuned)               | NA     |
|XGBoost                             | NA     |
|XGBoost (fine-tuned)                | NA     |
|LightGBM                            | NA     |
|LightGBM (fine-tuned)               | NA     |

### Pipeline:
 Data &rarr; Preprocessing: Standart Scaler* &rarr; Model
 
 *<sub>(StandardScaler standardizes a feature by subtracting the mean and then scaling to unit variance. Unit variance means dividing all the values by the standard deviation)</sub>

### Pytorh3D
|Model                               | MSE    |
|------------------------------------|--------|
|Model-1                             | NA     |
|Model-2                             | NA     |



### Conslusion:

Even the simple regression models shows good results. However, it is possible to improve model (assumption!) using to improve model using 3D input.
Current models were implemented  using 1D inputs.
