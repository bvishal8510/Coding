t = int(input())
for i in range(t):
	arr = list(map(int, input().split()))
	if (((arr[0]-1) % arr[2] == 0) and (((arr[1])-1) % arr[3] == 0)) or (((arr[0]-2) % arr[2] == 0) and ((arr[1]-2) % arr[3] == 0) and ((arr[0]-2) >= 0) and ((arr[1]-2) >= 0)):
		print("Chefirnemo")
	else:
		print("Pofik")