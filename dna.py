import sys

filename = sys.argv[1]

if not filename:
	print "Please specify file containing a DNA sequence"
	sys.exit

seq = open(filename, "r").read()

baseCounts = { 'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

for base in seq:
	if base in baseCounts:
		baseCounts[base] = baseCounts[base] + 1
	else:
		sys.exit("invalid base letter found in file.")

print baseCounts['A'],
print baseCounts['C'],
print baseCounts['G'],
print baseCounts['T']


