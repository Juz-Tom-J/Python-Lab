r = int(input("Enter the no. of rows: "))
c = int(input("Enter the no. of columns: "))

print("Matrix 1: ")
m1 = []

print("Enter the elements of matrix 1: ")
for i in range(r):
    x = []
    for j in range(c):
        x.append(int(input()))
    m1.append(x)

print("Matrix 2: ")
m2 = []

print("Enter the elements of matrix 2: ")
for i in range(r):
    y = []
    for j in range(c):
        y.append(int(input()))
    m2.append(y)
    
res = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        res[i][j] = m1[i][j]+m2[i][j]

for r in res:
    print(r)
