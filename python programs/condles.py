# n1 = int(input())
# n = input().lstrip().rstrip()
# l = n.split(' ')
# count = l.count(max(l))
# print(count)
n = input()
l = list(map(int, input().strip().split(' ')))
print(l.count(max(l)))