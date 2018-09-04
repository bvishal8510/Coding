n = int(input())
array = list(map(int, input().split()))
d = {}
count = 0
for i in array:
	d[i] += 1
	if d[i] == 2:
		count += 1
		d[i] = 0
print(count)