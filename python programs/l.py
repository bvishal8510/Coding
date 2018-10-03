line = input("Enter sentence   :").lower()
line1 = list(set(line.lower().split()))
line2=sorted(line1)
print(line2)

for i in line2:
	print(i,"----> ", line.count(i))
