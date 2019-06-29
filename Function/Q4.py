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

print ('operators are:','\n','+','\n','-','\n','*','\n','/','\n','%','\n','//')

n1=int(input('enter first number'))
o=input('enter operator')
n2=int(input('enter second number'))

if o == '+':
    print('=',add(n1,n2))

if o == '-':
    print('=',sub(n1,n2))

if o == '*':
    print('=',mul(n1,n2))

if o == '/':
    print('=',div(n1,n2))

if o == '%':
    print('=',mod(n1,n2))

if o == '//':
    print('=',floor(n1,n2))
