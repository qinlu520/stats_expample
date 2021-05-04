import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 6)
y = 2*x + 1

plt.figure()
plt.xlim(-3, 3)
plt.ylim(-6, 8)

plt.plot(x, y)

# gca =' get current axis'
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置默认坐标轴为 底轴  和  左轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# x轴(底轴) 位于Y轴的 0 处
ax.spines['bottom'].set_position(('data', 0))
# Y轴(左轴) 位于X轴的 0 处
ax.spines['left'].set_position(('data', 0))

# 增加注释
x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

plt.annotate(r'$2x+1=%s$'% y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30))
plt.show()
