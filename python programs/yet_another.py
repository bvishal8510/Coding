def maxSubarrayXOR(arr,n): 
  
    ans = -2147483648     #Initialize result 
   
    # Pick starting points of subarrays 
    for i in range(n): 
          
        # to store xor of current subarray 
        curr_xor = 0 
   
        # Pick ending points of 
        # subarrays starting with i 
        for j in range(i,n): 
          
            curr_xor = curr_xor ^ arr[j] 
            ans = max(ans, curr_xor) 
          
      
    return ans 


n,m = list(map(lambda x : int(x), input().split()))
l = []
size_list = []
for y in range(m):
	a,b = list(map(lambda x : int(x), input().split()))
	if l == []:
		l.extend([[a,b]])
		size_list.append(2)
	else:
		for i in range(len(l)):
			if (a in l[i]):
				l[i].append(b)
				size_list[i] += 1
				break
			if (b in l[i]):
				l[i].append(a)
				size_list[i] += 1
				break
		else:
			l.extend([[a,b]])
			size_list.append(2)
print(l)
print(size_list)

print(maxSubarrayXOR(size_list, len(size_list)))

