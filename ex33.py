from ex33class import callMe 	# Importing ex33class callMe

numbers = []

feedback = int(raw_input("> "))			# Gathering input for the end range of the list, gather feehback as int
numbers = callMe(feedback, 0, numbers)	# Inputs are list length, beggining value for i, and the list 'numbers'

print "The numbers: "

for num in numbers:
	print num
