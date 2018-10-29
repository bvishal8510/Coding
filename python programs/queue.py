def calculate_time(time,l,l1,ans,n):
	for i in range(n):
		if((time-l1[i]-ans) < 0):
			ans = time-l1[i]
		elif(time <= l1[i]):
			ans = 0
		time += l
	return [ans,time]

t = input()
for _ in range(t):
	n,m,k,l = [int(x) for x in raw_input().split()]
	l1 = [int(x) for x in raw_input().split()]
	l1.sort()
	time = l*(m+1)
	ans = float('inf')
	ans1,time1 = calculate_time(time,l,l1,ans,n)

	if((time1-k-ans1) < 0):
		ans1 = time1-k
	elif(time1 <= k):
		ans1 = 0
	print ans1
