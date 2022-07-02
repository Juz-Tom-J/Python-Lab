import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
z = abs(y)

plt.title("Rectifier Graph")
plt.plot(x,y)
plt.plot(x, z)
plt.show()
