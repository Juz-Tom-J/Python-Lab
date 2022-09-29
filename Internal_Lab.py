import matplotlib.pyplot as plt
import numpy as np

n = int(input("Enter the value of n: "))
x = np.linspace(-2*np.pi,2*np.pi,1000)
u = n*x
y = np.sin(u)/x
plt.plot(y)
plt.title("sin(nx)/x")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
