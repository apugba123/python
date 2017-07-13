#def while_loop(number1, number2):
#	i = number1
#	while (i < number2):
#		i = i + 1
		#if (i % 2 == 0):
#		print i 

def print_two_numbers(begin, end):
	#for i in reversed(range(begin, end)): //
	for i in range(end, begin, -1): 
		if (i % 2 == 0):
			print i
		
	
print_two_numbers(4, 10)	
#while_loop(4, 10)


	
	
