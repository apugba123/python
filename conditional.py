i = 8
if(i % 2):
	print "odd number"
else:
	print "even number"
	
	
print "\n"
def is_even (i):
	return i % 2 ==0
	
def sum_even (numbers):
	acc = 0
	for i in (numbers):
		if (i % 2 ==0):
			acc = acc + i
	return acc
		
sum_even([0,1,2,3,4,5,6,7,8,9,10])
