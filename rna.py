# Convert a DNA sequence to corresponding RNA sequence.
#
import sys

if len(sys.argv) < 2 or not sys.argv[1]:
    print "Please specify file containing a DNA sequence"
    sys.exit()

DNAseq = open(sys.argv[1], "r").read()

RNAseq = DNAseq.replace('T', 'U')

with open("rna.txt", "w") as RNAfile:
    RNAfile.write(RNAseq)

print "done"

