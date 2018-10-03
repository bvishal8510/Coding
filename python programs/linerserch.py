size=input("Enter the size of list :")
print "Enter the element one after the other."
l=[]
for i in range(size):
    l.append(raw_input())
ch=raw_input("Enter the element to be searched.")
c1=1
c2=0
for i in l:
    if (i==ch):
        print ch,"is found at ",c1,"position."
        c2+=1
    c1+=1
if (c2==0):
    print "Match not found."
        
