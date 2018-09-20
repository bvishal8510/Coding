import itertools
l1 = list(map(lambda x : int(x), input().split()))
l = []
count = 0
for i in range(l1[0]):
	l.append(int(input()))
for j in range(l1[0]):
	a = list(itertools.combinations(l,j))
	for k in a:
		sum1 = sum(k)
		if sum1 >= l1[1] and sum1 <= l1[2]:
			count += 1
print(count)