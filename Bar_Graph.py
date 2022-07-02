import  matplotlib.pyplot as plt
langs = ['C', 'C++', 'Java', 'Python','PHP']
students = [23, 17, 35, 29, 12]
plt.title("BAR GRAPH")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.bar(langs, students)
plt.show()
