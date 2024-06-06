import numpy as np
import matplotlib.pyplot as plt
from pydmd import DMD
from sklearn.metrics import mean_squared_error

def apply_dmd(data, svd_rank=2):
    dmd = DMD(svd_rank=svd_rank)
    dmd.fit(data)
    return dmd

def predict(dmd, steps):
    future_dynamics = dmd.reconstructed_data(real_only=True)[:, -1]
    for _ in range(steps):
        future_dynamics = np.append(future_dynamics, dmd.predict(future_dynamics[-dmd.modes.shape[0]:], 1)[-1])
    return future_dynamics

if _name_ == "_main_":
    snapshots = np.load("../data/AAPL_snapshots.npy")
    dmd = apply_dmd(snapshots)
    predicted = predict(dmd, 10)
    actual = snapshots[:, -10]

    plt.figure(figsize=(12, 6))
    plt.plot(range(len(snapshots[0])), snapshots[-1], label='Actual')
    plt.plot(range(len(snapshots[0]) - 10, len(snapshots[0])), predicted[-10:], label='Predicted')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    mse = mean_squared_error(actual, predicted[-10:])
    print(f'Mean Squared Error: {mse}')
