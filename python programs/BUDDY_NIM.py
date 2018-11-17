t = int(input())
for _ in range(t):
    n,m,x,y = list(map(lambda x : int(x), input().split()))
    ways = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            done = 0
            if (i != x) or (j != y):
                ways += ((n-1)*(m-1)) - (n-1)
                if (abs(i-x) == abs(j-y)):
                    if x > i:
                        ways += (n-x)
                    else:
                        ways += (x-1)
                    done = 1
                elif (x+y) == (i+j):
                    if x > i:
                        ways += (n-x)
                    else:
                        ways += (x-1)
                    done = 1
                elif (i - x) == 0:
                    if x > i:
                        ways += (n-x)
                    else:
                        ways += (x-1)
                    done = 1
                elif (j - y) == 0:
                    if y > j:
                        ways += (m-j)
                    else:
                        ways += (j-1)
                    done = 1
                if done == 0:
                    ways -= 1
    print(ways)