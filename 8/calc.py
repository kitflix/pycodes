print("Please select your desired operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
ab = int(input("enter your choice"))
a = int(input("Enter first no"))
b = int(input("Enter second no"))
if ab == 1:
     print("you've chosen additon")
     c = a + b
     print("result {0} + {1} = {2}".format(a,b,c))

if ab == 2:
     print("you've chosen subtraction")
     c = a - b
     print("result {0} - {1} = {2}".format(a,b,c))

if ab == 3:
     print("you've chosen multiplication")
     c = a * b
     print("result {0} X {1} = {2}".format(a,b,c))

if ab == 4:
     print("you've chosen divison")
     c = a / b
     print("result {0} / {1} = {2}".format(a,b,c))
