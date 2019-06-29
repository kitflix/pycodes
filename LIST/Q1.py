li=['apple','xyz','fizz','we','fizz']
n=li.count('fizz')
print (n)

'''
##other method##

li=['apple','xyz','fizz','we','fizz']
count=0
n=len(li)
for i in range(n):
    if 'fizz' in li[i]:
        count+=1

print (count)
'''

'''
##other method##

li=['apple','xyz','fizz','we','fizz']
count=0
n=len(li)
for i in range(n):
    if li[i]=='fizz':
        count+=1

print (count)
'''

'''
##other method##

li=['apple','xyz','fizz','we','fizz']
count=0
n=len(li)
for i in range(n):
    if li[i] is 'fizz':
        count+=1

print (count)
'''

