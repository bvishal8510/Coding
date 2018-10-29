t = int(input())
for y in range(t):
	l1 = list(map(lambda x : int(x), input().split()))
	n = l1[0]
	k = l1[1]
	a = [0] * k
	diff = n - int((k*(k+1))/2)
	j = k-1
	pro = 1
	if k == 1:
		print(n*(n-1))
		continue
	if((k*(k+1))/2 <= n):
		for i in range(k-1,-1,-1):
			a[i] = i+1 + int(diff/k)
	        # a[i] += int(diff/k)
		for i in range(0,diff%k):
			a[j] += 1
			j -= 1
		for i in range(0,k):
			pro *= (a[i]*(a[i] - 1))
	   p rint(pro%((10**9)+7))
	else:
		print(-1)