import random as r

print("COIN TOSS")
occ_list = []

def toss(n):
    occ = 0
    for i in range(0,n):
        occ_list.append(r.randint(0,1))
        if (occ_list[i] == 1): 
            occ+= 1
            print("Toss %d showed head"%(i+1))
        else:
            print("Toss %d showed tail"%(i+1))
    return occ,occ/n


option = int(input("Enter the value for number of tosses: "))
heads,prob = toss(option)
print("Number of heads occuring = ",heads)
print("Probability of getting heads = ",prob)
