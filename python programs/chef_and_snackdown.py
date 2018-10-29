t = int(input())
years = [2010,2015,2016,2017,2019]
for y in range(t):
	year = int(input())
	if (year == 2010) or (year == 2015) or (year == 2016) or (year == 2017) or (year == 2019):
		print("HOSTED")
	else:
		print("NOT HOSTED")
