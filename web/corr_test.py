import numpy as np
import pandas as pd

data = pd.DataFrame({'A': np.random.randint(1, 100, 10),
                     'B': np.random.randint(1, 100, 10),
                     'C': np.random.randint(1, 100, 10)})
print(data)
print('*'*30)
print(data.corr())  # 计算pearson相关系数 皮尔森相关系数
print('*'*30)
print(data.corr('kendall'))  # Kendall Tau相关系数
print('*'*30)
print(data.corr('spearman'))     # spearman秩相关
