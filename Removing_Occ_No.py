n = int(input("Enter the number of elements: "))
l = []
input("Enter the elements: ")

for i in range(n):
    l.append(int(input(" ")))

rem = int(input("Enter the number you want to remove: "))

while rem in l:
    l.remove(rem)

print("Updated list",l)
