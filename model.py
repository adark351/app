import pandas as pd
import numpy as np
import joblib 
import xgboost
model=joblib.load('regression_model.sav')
X_new = pd.DataFrame([[1217.70, 1, 0, 0, 0, 0]], columns=['Total Price', 'usage_Basic', 'usage_Entertainment', 'usage_Gaming', 'usage_High Performance', 'usage_Productivity'])
def predict(X_new):
    one_df12=pd.read_csv('one.csv')  
    y_pred_newh=model.predict(X_new)
    columns12 = [22,23,24,25,26,27,28]
    original_columns = [
        'CPU_speed', 'CPU_coreCount', 'CPU_threadCount', 'CPU_power', 'CPU_core_count',
        'CPU_core_clock', 'CPU_boost_clock', 'Memory_speed/0', 'Memory_speed/1',
        'Memory_modules/0', 'Memory_modules/1', 'PowerSupply_wattage', 'GPU_memory',
        'GPU_boost_clock'
    ]


    
    top_rows_list = []
    original_data=one_df12[original_columns]
        # Loop over each predicted entry
    for pred_entry in y_pred_newh:
        # Compute Euclidean distances
            euclidean_distances = np.linalg.norm(original_data.values - pred_entry, axis=1)

        # Get the index of the row with the smallest Euclidean distance
            min_distance_index = np.argsort(euclidean_distances)[:5]

        # Get the row with the smallest distance for this predicted entry
            top_row = one_df12.iloc[min_distance_index]
        
        # Append to the list
            top_rows_list.append(top_row)

    # Convert the list of rows to a single DataFrame
    top_rows_combined = pd.concat(top_rows_list,axis=0)
    return top_rows_combined