l=[]
new_l=[]
n = int(input("Enter the number of elements in the list : "))
for i in range(0,n):
    print("Enter the element",i+1,":",end = " ")
    l.append(int(input()))
print(l)

r = int(input("Enter the element to be removed : "))
for i in range(0,n):
    if(l[i]!=r):
        new_l.append(l[i])
print("New List :",new_l)
