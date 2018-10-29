t = int(input())
for y in range(t):
	l1 = list(map(lambda x : int(x), input().split()))
	l2 = list(map(lambda x : int(x), input().split()))
	if (len(l2) - l2.count(1)) <= l1[1]:
		print("YES")
	else:
		print("NO")