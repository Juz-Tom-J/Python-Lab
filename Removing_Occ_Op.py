l = map(int,input("Enter the numbers: ").split())

n = int(input("Enter the number to remove: "))

for i in l:
    if (i!=n):
        print(i)
