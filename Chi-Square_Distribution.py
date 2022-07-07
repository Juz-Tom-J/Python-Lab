#Program to do compute Chi-square value for calculation of dependency of education level and gender

Female = [60,54,46,41] #Female row
F_Total = 201 #Female Total
Male = [40,44,53,57] #Male row
M_Total = 194 #Male Total
Total = [100,98,99,98] #Total of each column
T_Total = 395 #Grand Total

Female_Exp = [] #Expected female value
Male_Exp = [] #Expected male value

fval = 0 
for i in Total:
    fval = i*(F_Total/T_Total)
    Female_Exp.append(fval)
print("Expected value for females: ",Female_Exp)

mval = 0
for i in Total:
    mval = i*(M_Total/T_Total)
    Male_Exp.append(mval)
print("Expected value for males: ",Male_Exp)

f=m=0 #Chi-Square values to 0
for i in range(0,4):
    f+=pow((Female[i]-Female_Exp[i]),2)/Female_Exp[i]
    m+=pow((Male[i]-Male_Exp[i]),2)/Male_Exp[i]

print("Female Chi-Square value:",f)
print("Male Chi-Square value:",m)
print("Mean Chi-Square value:",f+m)
-----------------------------------------------------------------------------------------
#Verification

import scipy.stats as stats

check = stats.chisquare((Female+Male),(fval+mval))

lst = list(check)
print(f"Chi Square value: {round((f+m), 4)}") #Checking through scipy stats

if lst[1] > 0.05:
    print(f"We accept null hypothesis, since {round(lst[1], 5)} > 0.05")
else:
    print("We reject null hypothesis")
