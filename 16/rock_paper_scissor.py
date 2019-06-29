import time
import random
print("Welcome to Rock Paper and Scissors Game")
a = int(input("Enter a number for 1.Rock 2.Paper 3.Scissors"))
if a == 1:
     print("You've given Rock")
if a == 2:
     print("You've given paper")
if a == 3:
     print("You've given Scissors")

print("Taking computers opinion...")
time.sleep(3)
b = random.randint(1,3)
if b == 1:
     print("PC has given Rock")
if b == 2:
     print("PC has given paper")
if b == 3:
     print("PC has given Scissors")


