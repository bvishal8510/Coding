from itertools import permutations
t = int(input())

for i in range(t):
    l = []
    st = input()
    for j in range(len(st)):
        l.append(j)
    l2 = list(permutations(l))
    for m in range(0,len(l2)):
        str2 = ''
        for n in l2[m]:
            str2 += st[n]
        c = 0
        if(str2 == str2[::-1]):
            c += 1
            for a in l2[m]:
                print((a+1),end=' ')
            print()
            break
    if(c == 0):
        print('-1')
