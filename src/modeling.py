from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def evaluate_regression(y_true, predictions):
    
    rmse = np.sqrt(mean_squared_error(y_true, predictions))
    
    r2 = r2_score(y_true, predictions)
    
    return rmse, r2
