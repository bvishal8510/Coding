k = int(input())
z = 0
for i in range(n):
	t = int(input())
	if t%k == 0:
		z += 1
print(z)

