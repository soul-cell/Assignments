l1=[1,2,3,5,6,4,5,56,546,57,5]
l2=[5,6,7,4]
z=[]
if(len(l1)>len(l2)):
    for i in range(len(l2),len(l1)):
        l2.insert(i,0)
elif(len(l1)<len(l2)):
    for i in range(len(l1), len(l2)):
        l1.insert(i, 0)
for i in range(len(l1)):
    x=l1[i]+l2[i]
    z.append(x)
print(z)
