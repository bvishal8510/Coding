t = int(input())
for i in range(t):
 	total_time = 0.0
 	n = int(input())
 	d = {}
 	for j in range(n):
 		word = input()
 		track_array = []
 		time = 0.0
 		if word in d:
 			total_time += (d[word]/2)
 		else:
 			for k in range(len(word)):
 				if (k == 0):
 					time += 0.2
 					if (ord(word[k]) <= 102):
 						track_array.append(1)
 					else:
 						track_array.append(2)
 				else:
 					if (ord(word[k]) <= 102):
 						track_array.append(1)
 						if (track_array[k-1] == 1):
 							time += 0.4
 						else:
 							time += 0.2
 					elif (ord(word[k]) > 102):
 						track_array.append(2)
	 					if (track_array[k-1] == 2):
 							time += 0.4
 						else:
 							time += 0.2
 			d[word] = time
 			total_time += time
 	print(round(total_time * 10))