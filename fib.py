# Calculate a modified Fibonaci number to simulate rabbit breeding
#
import sys

if len(sys.argv) != 3:
    print "Please specify number of months and number of rabbits per generation"
    sys.exit()

n = int(sys.argv[1])
k = int(sys.argv[2])

print ("Calculating for n = %d and k = %d" % (n, k))

if n < 3:
    print 1
    sys.exit()

f_n_minus_1 = 1
f_n_minus_2 = 1

# loop from 3 to n incrementing our f_n values as we go
for gen in range(3, n + 1):
    n = f_n_minus_1 + k * f_n_minus_2
    f_n_minus_2 = f_n_minus_1
    f_n_minus_1 = n

print f_n_minus_1



