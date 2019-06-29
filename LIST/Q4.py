l1=[2,3,5,3,6]
l2=['d','g','u','k','o']
#l3=[]
print (l1,'\n',l2)
n=len(l1)
l3=l2
print (l3)
for i in range(n):
    l2[i]=l1[i]
for i in range(n):
    l1[i]=l3[i]
    print(l1[i],l3[i])
    
print (l1,'\n',l2)
