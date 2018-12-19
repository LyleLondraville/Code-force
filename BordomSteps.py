dic = {}
dic2 = {}

nada = []
steps = []

total = 0
n = 0

dicKey = dic.keys
dicUpdate = dic.update
nadaAppend = nada.append

i2 = raw_input('')
i1 = raw_input('')

#steps = [1, 2, 1, 3, 2, 2, 2, 2, 3]

for i in range(0, len(i1)):
	itm = i1[i]

	if itm == ' ':
		steps.append(int(i1[n:i]))
		n = i + 1
	else :
		pass

steps.append(int(i1[n:len(i1)]))



for s in sorted(steps) :
	if s in dicKey():
		dic[s] += 1
	else :
		dicUpdate({s:1})

for x, y in dic.iteritems():
	dic2.update({ x*y : x })



for s in sorted(dic2.keys(), reverse = True):
	
	if (dic2[s] + 1 not in nada):
 		if ((dic2[s] - 1) not in nada):
			total += s 
			nadaAppend(dic2[s])


print total





















