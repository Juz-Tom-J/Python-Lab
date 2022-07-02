import  matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
res = []
for i in x:
    y = pow(i,4)+5
    res.append(y)
    
print("Input: ", x, "\nCalculated values:", res)
plt.plot(res)
plt.title("Normal Graph")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid()
plt.show()
