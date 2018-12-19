i2 = raw_input('')
i1 = raw_input('')


items = []
tempItems = []
stacks = []
n = 0

def srt(lis):
	string  = ''
	for i in sorted(lis, reverse = True):
		string += (str(i) + ' ')
	print (string[0:len(string) - 1])


for i in range(0, len(i1)):
	itm = i1[i]

	if itm == ' ':
		stacks.append(int(i1[n:i]))
		n = i + 1
	else :
		pass


stacks.append(int(i1[n:len(i1)]))
high = max(stacks)


for i in stacks:
	if i == high:
		tempItems.append(i)

		for x in range(i - 1, 0, -1):
			if x in items:
				tempItems.append(x)
				items.remove(x)
				n += 1
			else :
				break 
		
		srt(tempItems)
		high = min(tempItems) - 1
		tempItems[:] = []

	else :
		print ''
		items.append(i)
	














