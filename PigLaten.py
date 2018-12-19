string = raw_input()

count = 0

createdList = []
createdListAppend = createdList.append

for i in string:

	strLen = len(string)
	
	if string not in createdList:
		createdListAppend(string)
		count += 1
	
	string = string[strLen-1:strLen] + string[0:strLen-1]

print count 