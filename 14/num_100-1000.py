numbers = (input("Enter first Number"),input("Enter sencond Number"),input("Enter third Number"))


count = 0
for x in numbers:
    if (100<x<1000):
        count +=1
print("numbers", count)
