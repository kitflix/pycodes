n=int(input('enter a number'))

def add(x):
    y=x
    z=0
    x1=0
    for i in range(3):
        x=z+y
        x1=x1+x
        z=x*10
        print (x,x1)
    return x1

result=add(n)
print (result)
