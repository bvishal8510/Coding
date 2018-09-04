n = int(input())
array = list(map(int, input().split()))
max1 = 0
max_number = 0
for i in set(array):
	if array.count(i) > max1:
		max1 = array.count(i)
		max_number = i

print(max_number)