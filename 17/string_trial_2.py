a = "sr no,date,time,name,125"
print(len(a))

print(a.lower())

print(a.upper())

b = a.replace('H','M')
print (b)

d = a.split(',')
print (d[4])

e = int(d[4])
print (e*100)
