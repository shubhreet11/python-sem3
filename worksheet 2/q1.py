l=[11, 12, 13,14]
l. append (50)
l. append (60)
l. remove (11)
l. remove (13)
print (l)
l.sort()
print (l)
l. sort (reverse=-1)
print (1)
flag=-5
for i in range(0, len (1)):
    if(l[i]==13):
        flag=i
    else:
        None
if (flag==-5):
    print ("ELEMENT NOT FOUND" )
else:
    print ("LEMENT FOUND AT INDEX: ")
length=len (1)
print ("LENGTH OF LIST: ", length)
sum=0
sume=0
sumo=0
for i in range(0, len (l)):
    sum=sum+l[i]
    if[1[1]%2==0]:
        sume=sume+l[i]
    else:
        sumo=sumo+l[i]
print ("SUM OF ELEMENTS:", sum)
print("SUM OF EVEN ELEMENTS: ", sume)
print ("SUM OF ODD ELEMENTS: ", sumo)
sump=0
for i in range (0,len(l)):
    flagag=0
    for j in range (2,len[l]-1):
        if(l[i]%j==0):
            flag=1
        else:
            None
    if (flag==1):
        None
    else:
        sump=sump+1[i]
print ("SUM OF PRIME NUMBERS : ",sump)
l.clear()
print ("LIST CLEAR ")
print("l = ",l)
del l
print ("LIST DELETED" )