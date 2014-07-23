import sys

filename = sys.argv[1]

if not filename:
	print "Please specify file containing a DNA sequence"
	sys.exit

seq = open(filename, "r").read()

# Use a dictionary to store counts. Could use seperate variables but this
# saves a set of 'if' tests as we can reference the counts directly.
baseCounts = { 'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

for base in seq:
	if base in baseCounts:
		baseCounts[base] += 1
	else:
		sys.exit("invalid base letter found in file.")

# Print the items by key, iterating is not a good idea as the order 
# is not determinstic.
print baseCounts['A'],
print baseCounts['C'],
print baseCounts['G'],
print baseCounts['T']


