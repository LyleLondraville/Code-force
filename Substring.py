a = raw_input('')
b = raw_input('')

if len(a) == len(b):
	if a == b :
		print -1
	else :
		print len(a)

else :
	if len(a) > len(b):
		print len(a)
	else :
		print len(b)


