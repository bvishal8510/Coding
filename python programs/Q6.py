line = input("Enter sentence   :").lower()
line1 = list(set(line.lower().split()))

for i in line1:
    print(i , "----> " , line.count(i))

print (" ".join(sorted(line1)))
# words = [word for word in line.split(" ")]
# print (" ".join(sorted(list(set(words)))))
