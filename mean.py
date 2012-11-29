$This program find the mean of each row in the input arguments

import sys

sum = 0
n = 0

if len(sys.argv) == 1:
	print 'Error: No arguments given.'
	sys.exit()

for num in open(sys.argv[1:]):
	sum += float(num)
	n += 1

print sum / n

