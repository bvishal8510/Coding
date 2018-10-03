n = int(input())
no_on_chocolate = list(map(int, input().split()))
birth_d_and_m = list(map(int, input().split()))
count = 0

for i in range(len(no_on_chocolate)-(birth_d_and_m[1]-1)):
	total_count = 0
	for j in range(birth_d_and_m[1]):
		total_count += no_on_chocolate[i+j]
	print(total_count,",",birth_d_and_m[0])
	if total_count == birth_d_and_m[0]:
		count += 1

print(count)