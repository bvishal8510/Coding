n = int(input())
l = list(map(int, input().split()))
c = 1
max = 0
min = 0
count_max = 0
count_min = 0
for i in l:
	if c == 1:
		max = i
		min = i
	else:
		if i < min:
			count_min += 1
			min = i
		elif i > max:
			count_max += 1
			max = i
	c += 1
print(count_max," ",count_min)