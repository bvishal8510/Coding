t = int(input())
c = 0
for i in range(t):
	st1 = list(input())
	st2 = list(input())
	if 'b' in st1 or 'b' in st2:
		try:
			index = st1.index('b')
		except:
			index = st2.index('b')
		del st1[index]
		del st2[index]
		if 'o' in st1 or 'o' in st2:
			try:
				index = st1.index('o')
			except:
				index = st2.index('o')
			del st1[index]
			del st2[index]
			if 'b' in st1 or 'b' in st2:
				try:
					index = st1.index('b')
				except:
					index = st2.index('b')
				del st1[index]
				del st2[index]
				if st1 == [] and st2 == []:
					print('yes')
					c += 1
	if c == 0:
		print('no')
	c = 0

