no_of_pages = int(input())
page = int(input())
count = 0
i = 0
if page <= int(no_of_pages/2):
	i = 0
	if page != 1:
		while(1):
			count +=1
			if page == i or page == (i+1):
				break
		i += 2
else:
	i = no_of_pages
	if no_of_pages % 2 == 0:
		if page == i:
	else:
		pass                                     //incomplete
