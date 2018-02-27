nl=[]
for x in range(1500, 4500):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
