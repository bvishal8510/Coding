from random import *

n = int(input())
p = []
for i in range(n):
	p.append(str(i+1))
d = {}
for k in range(3*n):
	for i in range(n):
		j = randint(1,n)
		p[i],p[j-1] = p[j-1],p[i]
		s = " ".join(p)
		if s in d:
			d[s] += 1
		else:
			d[s] = 1

j = 0
for i in d:
	j += 1
	if j == 1:
		mav = d[i]
		miv = d[i]
		max_value = i
		min_value = i
	else:
		if d[i] > mav:
			max_value = i
		if d[i] < miv:
			min_value = i

print(max_value)
print(min_value)