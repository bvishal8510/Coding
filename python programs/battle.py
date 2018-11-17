t = int(input())
for _ in range(t):
    l1 = list(map(lambda x : int(x), input().split()))
    for y in range(l1[0]):
        l2 = list(map(lambda x : int(x), input().split()))
        l.extend([l2])
    ans_list = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 1:
                
