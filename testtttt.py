import pandas as pd
import numpy as np
from pandas.core import resample
data = pd.DataFrame({'key':
['a', 'b', 'c'] * 4, 'value': np.arange(12.)})
G=data.groupby('key').value
print(G.transform(lambda x:x.rank(ascending=False)))

ts = pd.date_range('1/1/2019', periods=5, freq='M')
df = pd.DataFrame({'num':np.arange(len(ts))},index=ts)
print(df.groupby(resample.TimeGrouper(freq='2M')).sum())