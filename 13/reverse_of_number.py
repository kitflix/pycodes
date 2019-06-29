a = int(input("Enter a number"))
print ("You've entered ",a)
rev = 0
while a > 0:
     rem = a % 10
     rev = (rev * 10) + rem
     a = a // 10
print("Your reverse num = ",rev)
