import re
import datetime

# pattern = re.compile("^[1-2][0-9]{6}[dD]?$")
#^[1][5-8]\d{5}[Dd]{0,1}$
#^[1][5-8][0-8][0-6][0-2][0-9][0-9][Dd]{0,1}$
year = datetime.date.today().year
end = ''
start = ''

for i in range(year, year-4, -1):
	end += str(i % 10)
	i = int(i/10)
	start += str(i % 10)

st1 = "^["+start+"]["+end+"][0-4][0-4][0-1][0-9][0-9][-]?[mdlMDL]?$"    		# regex for student number workable for every year
print(st1)
pattern = re.compile(st1)
# print(pattern.match(string))
while(1):
	string = input("Enter year :")
	if (pattern.match(string)):
		print("match")
	else:
		print("No match")
		


