t = int(input())
for i in range(t):
	l1 = list(map(lambda x : int(x), input().split()))
	l2 = list(map(lambda x : int(x), input().split()))
	l2 = sorted(l2)
	l2  = l2[::-1]
	kth = l2[l1[1]-1]
	count = 0
	for i in l2:
		if i >= kth:
			count += 1

	print("count",count)