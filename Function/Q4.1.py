def add (num1=0,num2=0):
    return num1+num2

def sub (num1=0,num2=0):
    return num1-num2

def mul (num1=1,num2=1):
    return num1*num2

def div (num1=1,num2=1):
    return num1/num2

def mod (num1=1,num2=1):
    return num1%num2

def floor (num1=1,num2=1):
    return num1//num2

print ('operators are:','\n','+','\n','-','\n','*','\n','/','\n','%','\n','//','\n','=')
total=0
while True:
    n1=int(input('enter first number'))
    o=input('enter operator')
    n1=int(input('enter first number'))
        
    if o == '+':
        total=add(n1,total)

    if o == '-':
        total=sub(n1,total)

    if o == '*':
        if total == 0:
            total=1
        total=mul(n1,total)

    if o == '/':
        if total == 0:
            total=1
        total=div(n1,total)

    if o == '%':
        if total == 0:
            total=1
        total=mod(n1,total)

    if o == '//':
        if total == 0:
            total=1
        total=floor(n1,total)

    if o == '=':
        break

print ('total=',total)

