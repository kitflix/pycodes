a = int(input("enter first number"))
b = int(input("Enter second number"))
if a > b:
     print("a is larger")
     if a > 100:
          print("a is also greater than 100")
          if a > 1000:
               print ("a is greater than 1000 also")
          print("a is only greater than and not 1000")
     print ("Thats enough")

if a > b and a > 100 and a > 1000:
     print ("a is larger than b and 100 and 1000")

if b > a or b > 100 or b > 50:
     print ("b has something to print")
     
print("Code exiting")


#input 3 numbers from user and find the largest
# input 6 numbers from the user and find the largest and smallest
