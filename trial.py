t = int(input())
for i in range(t):
	count = 0
	n = int(input())
	arr = list(map(int, input().split()))
	even = []
	odd = []
	l_outer = []

	for j in range(len(arr)):
		if arr[j] % 2 == 0:
			even.append(arr[j])
		else:
			odd.append(arr[j])

	print("even",even)
	print("odd",odd)

	for j in range(len(even)-1):
		for k in range(j+1, len(even)):
			print("even",[even[j],even[k]],"  ",((even[j] | even[k]) and (~even[j] | ~even[k])))
			if (((even[j] | even[k]) & (~even[j] | ~even[k])) > 3):
				print("inner even")
				count += 1
				print("count",count)

	l_outer = []

	for j in range(len(odd)-1):
		for k in range(j+1, len(odd)):
			print("odd",[odd[j],odd[k]],"   ",((odd[j] | odd[k]) and (~odd[j] | ~odd[k])))
			if (((odd[j] | odd[k]) & (~odd[j] | ~odd[k])) > 3):
				print("inner odd")
				count += 1
				print("count",count)

	print(count)