import sys

if len(sys.argv) < 2 or not sys.argv[1]:
    print "Please specify file containing a DNA sequence"
    sys.exit()

DNA_seq = open(sys.argv[1], "r").read()

# reverse the sequence using the extended slice method. make it lower case too to aid in the base switching next.
rev = DNA_seq[::-1].lower()

# convert a -> T, t -> A, c -> G, g -> C
revc = rev.replace('a', 'T').replace('t', 'A').replace('c', 'G').replace('g', 'C')

with open("revc.out.txt", "w") as rev_file:
    rev_file.write(revc)

print "done"
