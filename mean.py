$This program find the mean of input values place after the command

import sys

sum = 0

if len(sys.argv) == 1:
	print 'Error: No arguments given.'
	sys.exit()

for num in sys.argv[1:]:
	sum += float(num)

print sum / (len(sys.argv) - 1)

