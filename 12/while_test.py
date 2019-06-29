'''
a = 0
while a < 10:
     print("a = ",a)
     a = a + 1
'''
a = 1
while a <= 3:
     b = int (input ("enter a no: "))
     if b == 0:
          print ("exiting loop with break command, 'else' is not executed")
          break
     a+=1
else:
     print ("loop exited without executing break command")
