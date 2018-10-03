def check(n):
	if n <= 0:
		if n == 0:
			return 1
		return 0
	sum = check(n-1) + check(n-2) + check(n-3)

n = int(input())
check(n)
print(n)
print(c)