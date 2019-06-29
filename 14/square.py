numbers = []
squares = []
cubes = []

# start and end numbers
start = 1 
end = 10 

# run a loop from start to end+1 
for count in range (start, end+1) :
    numbers.append (count)
    squares.append (count**2)
    cubes.append (count**3)

# print the lists
print "numbers: ",numbers
print "squares: ",squares
print "cubes  : ",cubes
