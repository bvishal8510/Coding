def gcd(a, b): 
    if (a == 0 or b == 0): 
            False
      
    if (a == b): 
        return a 
  
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 
      
def coprime(a, b) : 
    return (gcd(a, b) == 1) 

def numOfPairs(arr, n) : 
    count = 0
      
    for i in range(0, n-1) : 
        for j in range(i+1, n) : 
      
            if (coprime(arr[i], arr[j])) : 
                count = count + 1
      
    return count 




t = int(input())
for y in range(t):
	n = int(input())
	l1 = list(map(lambda x : int(x), input().split()))
	connected = []

	for i in range(len(l1)-1):
		for j in range(i+1,len(l1)):
			if (coprime(l1[i], l1[j])):
				

	count = 0
	length = 0
	temp = -1
	for i in range(len(l1)):
		if l1[i] == -1:
			count += 1
			if temp != -1:
				temp += 1
		else:
			if i == 0 or temp == -1:
				temp = l1[i]
			else:
				if l1[i] == (temp + 1):
					temp += 1
				else:
					break
		length += 1

	if count == n:
		print("inf")
	elif length == 1:
		print('impossible')
	else:
		print(length)