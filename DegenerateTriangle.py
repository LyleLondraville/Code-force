n1 = raw_input('')
index = 0
passed = False 
numbers = []

if int(n1) < 3 :
	print "NO"
else :
	n2 = raw_input('')
	
	for i in range(0, len(n2)):
		if n2[i] == ' ':
			numbers.append(int(n2[index:i]))
			index = (1 + i)
		else :
			pass 
	numbers.append(int(n2[index:len(n2)]))

numbers[:] = sorted(numbers, key = int)


index = 0 

while index < len(numbers) - 2:
	a = numbers[index]
	b = numbers[index + 1]
	c = numbers[index + 2]

	if a + b > c :
		passed = True 
		break 
	else :
		pass 

	index += 1

if passed == True:
	print "YES"
else :
	print "NO"













