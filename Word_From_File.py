f = open('word.txt', 'r+')

upcase = lowcase = spcl_sym = sen = 0

special = '!@#$%^&*()-+?_=,<>/"'

for w in f:
    sen = w.split('.')
    ws = w.split()
   
    for i in range(0, len(w)):
        if w[i].isupper():
            upcase+= 1
           
        elif w[i].islower():
            lowcase+= 1
           
        elif w[i] in special:
            spcl_sym+= 1
           
print("Number of words: ", len(ws))
print("Number of sentences: ", len(sen))
print("Number of uppercase letters: ", upcase)
print("Number of lowercase letters: ", lowcase)
print("Number of special symbols: ", spcl_sym)
f.close()
