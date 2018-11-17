t = int(input())
for _ in range(t):
    n,m,k = list(map(lambda x : int(x), input().split()))
    l2 = list(map(lambda x : int(x), input().split()))
    l2.sort()
    item = 0
    max_price = 0
    while(1):
    	if m < k:
    		max_price += l2[m-1]
    		break
    	else:
    		if m == item:
    			break
    		if (item + k + 1) > m:
    			max_price += l2[m-1]
    			break
    		else:
    			item += (k+1)
    			max_price += l2[item-1]
    print(max_price)