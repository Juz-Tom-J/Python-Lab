s = input('Enter the string: ')
s1 = input('Enter word to be replaced: ')
w = input('Enter word to replace: ')
new = ""
x = s.split()
for i  in x:
    if (i==s1):
        new=new+" "+w
    else:
        new=new+" "+i
print(new)
