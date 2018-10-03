def printarray(l2, l3):
	st=''
	for i in range(len(l2)):
		if l2[i] == 1:
			st += str(l[i]) + ' '
	if st not in l3:
		l3.append(st)

def subset(l2, index, l3):
	if 0 not in l2:
		return 1
	elif 1 not in l2:
		l2[s-1] = 1
		index = s-1
		return subset(l2, index, l3)
	else:
		if (l2[index-1] == 1) or (index == 0):
			l2[s-1] = 1
			index = s-1
			return subset(l2, index, l3)
		elif l2[index-1] == 0:
			l2[index] = 0
			l2[index-1] = 1
			index = index -1
			return subset(l2, index, l3)


s1 = int(input())
a = input()
l1 = a.split()
l1 = list(map(lambda x : int(x), l1))
l3 = []
l=[]
s = 0
for i in range(s1):
	s += 1
	index = -1
	l.append(l1[i])
	l2=[]
	for j in range(i+1):
		l2.append(0)
	subset(l2, index, l3)

for i in l3:
	print(i)