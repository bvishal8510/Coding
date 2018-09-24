import math
t = int(input())
pi = math.pi
while(t--):
	l = list(map(lambda x : int(x), input().split()))
	print(math.tan((l[2]*math.atan((l[0]/l[1])))%(2*pi)))