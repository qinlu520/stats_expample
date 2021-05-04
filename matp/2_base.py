import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

# figure
plt.figure(num=6, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 设置坐标轴取值范围、轴名称
plt.xlim(-1, 2)
plt.xlabel('I am X')
plt.ylim(-2, 3)
plt.ylabel('I am Y')

# 更改坐标轴 标尺 的取值范围 和map
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['really bad', 'bad', 'normal', 'good', 'really good'])

# gca =' get current axis'
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置默认坐标轴为 底轴  和  左轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# x轴(底轴) 位于Y轴的 -1 处
ax.spines['bottom'].set_position(('data', -1))
# Y轴(左轴) 位于X轴的 0 处
ax.spines['left'].set_position(('data', 0))
plt.show()
