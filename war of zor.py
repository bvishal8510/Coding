# import math
# t = int(input())
# for k in range(t):
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	arr = list(set(arr))
# 	result = 0
# 	l=[]
# 	even = []
# 	odd = []
# 	for i in arr:
# 		if (((2 | i) and (~2 | ~i)) in l) or (((0 | i) and (~0 | ~i)) in l):
# 			result += 1
# 		l.append(i)
# 		if i % 2 == 0:
# 			even.append(i)
# 		else:
# 			odd.append(i)

# 	total_even = 0
# 	total_odd = 0

# 	if len(even) >= 2:
# 		total_even = int(math.factorial(len(even))/(math.factorial(len(even)-2) * 2))

# 	if len(even) >= 2:
# 		total_odd = int(math.factorial(len(odd))/(math.factorial(len(odd)-2) * 2))

# 	print((total_odd + total_even) -result)

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

	for j in range(len(even)-1):
		for k in range(j+1, len(even)):
			if [even[j],even[k]] not in l_outer:
				if (((even[j] | even[k]) & (~even[j] | ~even[k])) > 3):
					count += 1
				l_outer.append([even[j],even[k]])

	l_outer = []

	for j in range(len(odd)-1):
		for k in range(j+1, len(odd)):
			if [odd[j],odd[k]] not in l_outer:
				if (((odd[j] | odd[k]) & (~odd[j] | ~odd[k])) > 3):
					count += 1
				l_outer.append([odd[j],odd[k]])

	print(count)