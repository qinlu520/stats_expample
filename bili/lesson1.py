import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

'''
集中趋势分析：
    均值、加权平均、众数、中位数
'''
data = pd.DataFrame({'value': np.random.randint(100, 120, 100),
                     'f': np.random.rand(100)})
data['f'] = data['f'] / data['f'].sum()  # f 是权重
print(data.head())
print('-'*30)
mean = data['value'].mean()
print('简单平均数: %.2f' % mean)
mean_w = (data['value'] * data['f']).sum() / data['f'].sum()
print('加权平均数: %.2f' % mean_w)
m = data['value'].mode()
print('众数: %.2f' % m)
md = data['value'].median()
print('中位数: %.2f' % md)
print(data['value'].describe())

