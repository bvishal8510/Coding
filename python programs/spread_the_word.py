t = int(input())
for i in range(t):
	num = int(input())
	l2 = list(map(lambda x : int(x), input().split()))
	day_count = 0
	people_know = 1
	total_people = len(l2)
	while(people_know < total_people):
		for i in range(people_know):
			people_know += l2[i]
		day_count += 1
	print(day_count)