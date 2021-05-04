import matplotlib.pyplot as plt
import numpy as np

# 图例
x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

plt.figure()

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

plt.plot(x, y2, label='up')
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')

# 图例 key word
plt.legend()

plt.show()
