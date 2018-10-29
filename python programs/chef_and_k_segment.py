t = int(input())
for y in range(t):
    l1 = list(map(lambda x : int(x), input().split()))
    n = l1[0]
    k = l1[1]
    l=[]
    for z in range(n):
        l2 = list(map(lambda x : int(x), input().split()))
        l.extend([l2])
    ss = ('0'*(n-k))+('1'*k)
    tr = 1
    ss_i = ''
    fmax = 0
    while(1):
        done = 0
        left = 0
        right = 10**9+1
        max1=0
        for j in range(-1,-(len(ss)+1),-1):
            if(ss[j] == '1'):
                if(l[j][0] > left):
                    left = l[j][0]
                if(l[j][1] < right):
                    right = l[j][1]

            if ss[j]=='0' and ss[j+1]=='1' and done==0 and j!=-1:
                ss_i = ss[0:len(ss)+j] + '1'
                count = k - (ss_i.count('1'))
                remain_length = n - len(ss_i)
                ss_i += '0'*(remain_length - count) + '1'*count
                done = 1
        ss = ss_i
        max1 = right - left
        if(fmax < max1):
            fmax = max1
        if done == 0:
            break
    print(fmax)