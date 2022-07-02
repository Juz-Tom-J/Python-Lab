import  matplotlib.pyplot as plt
x = [1,4,2,5,8,6]

plt.plot(x)
plt.title("Normal Graph")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid()
plt.show()

plt.figure()
plt.stem(x)
plt.title("Stem Graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
