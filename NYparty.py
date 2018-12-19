x = 0
c = 0
t = 0

inpu = raw_input()

for i in range(0, len(inpu)):
	char = inpu[i]

	if char == ' ':
		n = int(inpu[x:i])
		x = i + 1
		break 

k = int(inpu[x:len(inpu)])


tl = 240-k

while True:
	c += 1

	if t + 5*c <= tl and n >= c:
		t += (5*c)
	else :
		print c - 1
		break 

	
