t = int(input())
for y in range(t):
	n = int(input())
	l1 = list(map(lambda x : int(x), input().split()))
	count = 0
	length = 0
	temp = -1
	for i in range(len(l1)):
		if l1[i] == -1:
			count += 1
			if temp != -1:
				temp += 1
		else:
			if i == 0 or temp == -1:
				temp = l1[i]
			else:
				if l1[i] == (temp + 1):
					temp += 1
				else:
					break
		length += 1

	if count == n:
		print("inf")
	elif length == 1:
		print('impossible')
	else:
		print(length)