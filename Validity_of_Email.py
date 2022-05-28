e = input('Enter the email: ')
m = e.split("@")
domain = ["gmail.com","yahoo.com","outlook.com"]

for i  in m:
    for j in domain:
        if (i==j):
            flag = 1
            print("Valid email")
            break
        else:
            flag = 0

if (flag==0):
    print("Invalid email")
