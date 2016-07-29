# This file is for ex33 from LPTHW

import time # Importing time, which was used for the sleep function to assist with debugging

def callMe(test, i, numbers):
	while i < test:
		print i
		print test
		time.sleep(1)
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers 			# Returns the list for 'numbers'