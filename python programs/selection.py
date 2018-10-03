l=[]
n=input("Enter the number of names :")
for i in range(n):
    l+=[raw_input("Enter the name :")]
size=len(l)
for i in range(0,size-1):
    low=l[i]
    loc=i
    for j in range(i+1,size):
        if(low>l[j]):
            low=l[j]
            loc=j
    print l
    l[i],l[loc]=l[loc],l[i]

print "The sorted list is :",l
