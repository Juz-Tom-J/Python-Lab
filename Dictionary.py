d1 ={"The Da Vinci Code": 5,"Wings Of Fire": 3,"The Alchemist": 4}
print("\n1:Add stock\n2:Delete stock\n3:To add new book\n4:Exit")
n=int(input("Enter your choice: "))
while(n!=4):
    if(n==1):
        print(d1)
        z=input("Enter the  book name: ")
        y=int(input("Enter the no.of stocks you are adding: "))
        d1[z]=d1[z]+y
    elif(n==2):
        print(d1)
        z=input("Enter the book name: ")
        y=int(input("Enter the no.of stocks you are deleting: "))
        d1[z]=d1[z]-y
    else:
        print(d1)
        z=input("Enter the book name: ")
        u=int(input("Enter the no.of stocks: "))
        d1.update({z:u})
    print("\n1:Add stock\n2:Delete stock\n3:To add new book\n4:Exit")
    n=int(input("Enter your choice:"))
print(d1)
