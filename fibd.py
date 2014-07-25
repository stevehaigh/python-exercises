# Calculate a modified Fibonaci number to simulate rabbit breeding with mortal rabits
#
import sys

if len(sys.argv) != 3:
    print "Please specify number of months and number months a rabbit lives for"
    sys.exit()

n = int(sys.argv[1])
m = int(sys.argv[2])

print ("Calculating for n = %d and m = %d" % (n, m))

if n < 3:
    print n
    sys.exit()



