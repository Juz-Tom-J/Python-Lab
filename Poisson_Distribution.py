def checkFact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

l = float(input("Enter the value for average: "))
x = int(input("Enter the value for no. of occurences: "))
e = 2.71828

num = (pow(l,x))*(pow(e,-l))
den = checkFact(x)
poisson = float(num/den)
print("Poisson value: ",poisson)
