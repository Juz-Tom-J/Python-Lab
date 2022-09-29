n = int(input("Enter N for N x N matrix: "))
A = []
print("Enter the element for Matrix 1: ")
for i in range(n): 
    row = []
    for j in range(n):
        row.append(int(input()))             
    A.append(row)                              
print(A)
print("Display Array A In Matrix 1 Form")
for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print() 
B = []
print("Enter the element for Matrix 2: ")
for i in range(n): 
    row = []                                      
    for j in range(n):
        row.append(int(input()))            
    B.append(row)                            
print(B)
print("Display Array B In Matrix 2 Form")
for i in range(n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()                                      
result = [[0,0,0], [0,0,0], [0,0,0]] 
for i in range(n):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j] 
print("Resultant Matrix is: ")
for r in result: 
    print(r) 
