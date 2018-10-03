t = int(input())
for i in range(t):
	arr1 = list(map(int, input().split()))
	coin_index = arr1[1]
	for i in range(arr1[2]):
		arr2 = list(map(int, input().split()))
		if coin_index == arr2[0]:
			coin_index = arr2[1]
		elif coin_index == arr2[1]:
			coin_index = arr2[0]
	print(coin_index)
