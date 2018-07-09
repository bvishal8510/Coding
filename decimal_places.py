p_no = int(input())
s = input()
l = s.split()
l = list(map(lambda x : int(x), l))
length = len(l)
p_no = 0
z_no = 0
n_no = 0
for i in l:
	if i>0:
		p_no += 1
	elif i == 0:
		z_no += 1
	else:
		n_no += 1
print(round((p_no/length),6))
print(round((n_no/length),6))
print(round((z_no/length),6))