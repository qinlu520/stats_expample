import pandas as pd
import numpy as np

index = pd.date_range("1999/1/1", periods=1100)
ts = pd.Series(data=np.random.normal(0.5, 2, 1100), index=index)
# print(ts)
ts = ts.rolling(window=100, min_periods=100).mean().dropna()
print(ts.head())
