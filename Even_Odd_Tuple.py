x = tuple(map(int,input("Enter the numbers: ").split()))
odd_numbers = []
even_numbers = []
print("Enter the limit: ",x)
for i in range(len(x)):
    if(x[i]%2==0):
        even_numbers.append(x[i])
    else:
        odd_numbers.append(x[i])
print("Odd numbers: ",tuple(odd_numbers))
print("Even numbers: ",tuple(even_numbers))
