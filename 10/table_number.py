print("This is code for Finding out table of a number using for loop")
num = int(input("enter the number"))
print ("You've entered ",num)
for i in range(1,11):
     res = num * i
     print("{0} x {1} = {2}".format(num,i,res))
