a = int(input('Enter the 1st number: '))
b = int(input('Enter the 2nd number: '))
c = int(input('Enter the 3rd number: '))

largest = 0

if((a>b)and(a>c)):
    largest = a

elif((b>a)and(b>c)):
    largest = b

else:
    largest = c
    
print('The largest number is: ',largest)
