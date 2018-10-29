t = int(input())
for y in range(t):
	l1 = list(map(lambda x : int(x), input().split()))
	count = [0] * (l1[0] + l1[1] -2)
	l2 = []
	for j in range(l1[0]):
		w = input()
		for k in range(len(w)):
			if w[k] == '1':
				l2.extend([[j,k]])
	length = len(l2)

	for i in range(length-1):
		for j in range(i+1, length):
			count[(abs(l2[j][0] - l2[i][0]) + abs(l2[j][1] - l2[i][1])) - 1] += 1

	for i in count:
		print(str(i), end=' ')
	print()