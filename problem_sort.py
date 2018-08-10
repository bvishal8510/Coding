l = list(map(int, input().strip().split(' ')))
l3 = []
l4 = []
l5 = []
fa = []
n=0
for i in range(l[0]):
	l1 = list(map(int, input().strip().split(' ')))
	l2 = list(map(int, input().strip().split(' ')))
	for i in range(l[1]):
		l3.append(l1[i])
		l3.append(l2[i])
		l4.extend([l3])
		l3 = []
	l5.extend([l4])
	l4 = []
for i in range(len(l5)):
	n = 0
	l5[i] = sorted(l5[i])
	for j in range(len(l5[i])-1):
		if l5[i][j][1] > l5[i][j+1][1]:
			n += 1
	fa.extend([[n,i]])
fa = sorted(fa)
print(fa)
for i in fa:
	print(i[0]+1)