m1=int(input("Enter 1st number"))
m2=int(input("Enter 2nd number"))
m3=int(input("Enter 3rd number"))
m4=int(input("Enter 4th number"))
m5=int(input("Enter 5th number"))
 
large=m1
small=m2
if m2>large:
	large=m2
if m3>large:
	large=m3
if m4>large:
	large=m4
if m5>large:
	large=m5
print ("largest number is = ",large)
 
if m2<small:
	small=m2
if m3<small:
	small=m3
if m4<small:
	small=m4
if m5<small:
	small=m5
print ("smallest number is =",small)
