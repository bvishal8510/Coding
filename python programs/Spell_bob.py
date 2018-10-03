t = int(input("1"))
c = 0
for i in range(t):
	st1 = list(input("2"))
	st2 = list(input("3"))
	for j in range(3):
		if 'o' in st1:
			index = st1.index('o')	
			if st2[index] == 'b':
				if st1.count('b') > 2 or st2.count('b') > 2:
					print('yes')
					c += 1
					break
			if st2[index] != 'b':
				if st1.count('b') > 1 or st2.count('b') > 1:
					print('yes')
					c += 1
					break
			if st1.count('o') > 1:
				st1[index] = 'd'
			else:
				break

		elif 'o' in st2:
			index = st2.index('o')
			print("index o",index)
			if st1[index] == 'b':
				if st1.count('b') > 2 or st2.count('b') > 2:
					print('yes')
					c += 1
					break
			if st1[index] != 'b':
				if st1.count('b') > 1 or st2.count('b') > 1:
					print('yes')
					c += 1
					break
			if st2.count('o') > 1:
				st2[index] = 'd'
			else:
				break

		else:
			break

	if c == 0:
		print('no')
	c = 0

