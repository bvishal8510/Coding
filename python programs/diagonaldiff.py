import math

n=int(input())
l=[]
dia_sum1=0
dia_sum2=0
for i in range(n):
	s=input()
	l1=s.split()
	l1 = list(map(lambda x : int(x), l1))
	l.extend([l1])
for i in range(n):
	dia_sum1 += l[i][i]
	dia_sum2 += l[i][n-1-i]
diff = int(math.fabs(dia_sum1 - dia_sum2))
print(diff)
