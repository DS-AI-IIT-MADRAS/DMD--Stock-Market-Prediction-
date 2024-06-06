import pandas as pd
import numpy as np

def preprocess_data(file_path, window_size):
    data = pd.read_csv(file_path, index_col=0)
    snapshots = []
    for i in range(len(data) - window_size):
        snapshots.append(data.values[i:i + window_size])
    return np.array(snapshots).T

if _name_ == "_main_":
    file_path = '../data/AAPL_data.csv'
    window_size = 30
    snapshots = preprocess_data(file_path, window_size)
    np.save("../data/AAPL_snapshots.npy", snapshots)
