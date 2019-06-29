li=['ssss',10,'kkkk','ddd',30,'a']
n=len(li)
count=0
for i in range(n):
    if type(li[i]) is str:
        if len(li[i])>=2:
            count+=1
print (count)
