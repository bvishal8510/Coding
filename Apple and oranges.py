house = list(map(int, input().split()))
a_and_o_tree = list(map(int, input().split()))
no_of_a_and_o = list(map(int, input().split()))
a_co = list(map(int, input().split()))
o_co = list(map(int, input().split()))
a_count = 0
o_count = 0
for i in a_co:
	if (i+a_and_o_tree[0] >= house[0]) and (i+a_and_o_tree[0] <= house[1]):
		a_count += 1

for i in o_co:
	if (a_and_o_tree[1]+i >= house[0]) and (a_and_o_tree[1]+i <= house[1]):
		o_count += 1
print(a_count)
print(o_count)