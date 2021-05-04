import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2
# figure1
plt.figure()
plt.plot(x, y1)
# figure2
plt.figure()
plt.plot(x, y2)

# figure6
plt.figure(num=6,
           figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1, linestyle='--')
plt.show()
