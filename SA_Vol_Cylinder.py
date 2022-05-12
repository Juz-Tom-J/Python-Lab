def TotSurfAr(r,h):
    TSA = 2*3.14*r*(r+h)
    return TSA
 
def CurSurfAr(r,h):
    CSA = 2*3.14*r*h
    return CSA
 
def Volume(r,h):
    VOL = 3.14*r*r*h
    return VOL
 
r = float(input('Enter the radius: '))
h = float(input('Enter the height: '))

print('Total surface area: ',TotSurfAr(r,h))
print('Curved surface area: ',CurSurfAr(r,h))
print('Volume: ',Volume(r,h))
