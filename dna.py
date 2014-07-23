# Count the number of each base A,C,G and T in a file.
#
import sys

if len(sys.argv) < 2 or not sys.argv[1]:
    print "Please specify file containing a DNA sequence"
    sys.exit()

seq = open(sys.argv[1], "r").read()

# Use a dictionary to store counts. Could use separate variables but this
# saves a set of 'if' tests as we can reference the counts directly.
baseCounts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for base in seq:
    if base in baseCounts:
        baseCounts[base] += 1
    else:
        sys.exit("invalid base letter found in file.")

# Print the items by key, iterating is not a good idea as the order 
# is not deterministic.
print baseCounts['A'],
print baseCounts['C'],
print baseCounts['G'],
print baseCounts['T']


