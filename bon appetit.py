array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
sum_charged = int(input())
actual_sum = 0
for i in range(len(array2)):
	if i != array1[1]:
		actual_sum += array2[i]
actual_sum = int(actual_sum/2)
if actual_sum == sum_charged:
	print("Bon Appetit")
else:
	print(sum_charged-actual_sum)
