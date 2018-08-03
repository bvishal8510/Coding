def printarray(l):
	for i in range(len(l)):
		print(s[l[i]], end='')
	print()

def lengthk(l):
	printarray(l)
	if 0 not in l and 1 not in l:
		return 1
	elif l[k-1] >= k-1:
		k1 = k-1
		while(l[k1] >= (k-1) and k1 >= 0):
			l[k1] = 0
			print("k1",k1)
			print("1 ",l)
			k1 -= 1
			l[k1] += 1
		return lengthk(l)
	else:
		print("k",k)
		l[k-1] += 1
		print("2 ",l)
		return lengthk(l)


s = input()
l1 = s.split()
s = l1[0]
k = int(l1[1])
l=[]
for i in range(k):
	l.append(0)
lengthk(l)