import re
import datetime
# pattern = re.compile("^[1-2][0-9]{6}[dD]?$")
#^[1][5-8]\d{5}[Dd]{0,1}$
year1 = datetime.date.today().year
year2 = year1 - 3
year1 = str(year1)
print(year1)
print(type(year1))
print(year2)
st1 = "^[1][5-8]\d{5}[Dd]{0,1}$"
pattern = re.compile(st1)
string = "1610181"
print(pattern.match(string))