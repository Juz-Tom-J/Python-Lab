f = open('f1.txt', 'r+')
l = []
for i in f:
    l.append(int(i))
print("File contents: ",l)
print("Prime numbers: ", end="")
for j in l:
    if j == 0 or j == 1:
        continue
    for i in range(2, j//2 + 1):
        if j % i == 0:
            break
    else:
        print(j, end = " ")
f.close()
