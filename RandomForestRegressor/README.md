## Dependancy
```pip3 install -r requirements.txt```

## Random Forest Regressor Training&Inference 

#### Model training and validation:  
```python3 model_1.py --por <porosity file path> --res <resistivity file path> --sat <saturation file path>```  
current file run command: ```python3 model_1.py --por por.txt --res res.txt --sat sat.txt```

#### Model inference:  
```python3 model_1.py --test --por <porosity file path> --res <resistivity file path> --load_model <model file path>```  
current file run command: ```python3 model_1.py --test--por por.txt --res res.txt```

#### Model accuracy:
**MSE**: 0.0157

#### Output:
Output saves in ```saturation.csv```
