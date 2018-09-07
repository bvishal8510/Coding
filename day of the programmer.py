n = int(input())
if (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)) or n == 1800:
	print("12.09."+str(n))
else:
	print("13.09."+str(n))