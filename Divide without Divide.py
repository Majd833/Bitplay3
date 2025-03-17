def divide(divid,divis):
    #check if diviisor is +ve or -ve
    sign=(-1 if((divid<0)^(divis<0))else 1)
    #make both +ve
    divid=abs(divid)
    divis=abs(divis)
    quot=0
    temp=0
    #go from 31 to 0 and group all true bits
    for i in range (31,-1,-1):
        if(temp+(divis<<i)<=divid):
            temp+=divis <<i
            quot|=1<<i
    if sign==-1:
        quot=-quot
    return quot
divid=int(input("Enter a:"))
divis=int(input("Enter b:"))
print(divide(divid,divis))