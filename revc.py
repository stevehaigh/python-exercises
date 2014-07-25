# Convert a DNA sequence to corresponding reverse compliment sequence.
#
import sys

if len(sys.argv) < 2 or not sys.argv[1]:
    print "Please specify file containing a DNA sequence"
    sys.exit()

with open(sys.argv[1], "r") as DNAfile:
    DNAseq = DNAfile.read()

    # reverse the sequence using the extended slice method. make it lower case too to aid in the base switching next.
    rev = DNAseq[::-1].lower()

    # now convert a -> T, t -> A, c -> G, g -> C

    revc = rev.replace('a', 'T').replace('t', 'A').replace('c', 'G').replace('g', 'C')

    with open("revc.txt", "w") as revfile:
        revfile.write(revc)

print "done"
