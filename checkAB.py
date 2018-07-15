def check(n):
	if s[n] == 'c':
		return 1
	elif s[n] == 'a':
		return check(n+1)
	elif (s[n-1] == 'a') and (s[n] == 'b' and s[n+1] == 'b'):
		 return check(n+2)
	else:
		return 0


s = input()
s = s+'c'
if s[0] == 'a':
	c = check(1)
	if (c == 1):
		print("true")
	else:
		print("false")
else:
	print("false")