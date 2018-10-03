n=input()
k=input()
x=input()
o=x%k
i=n
while(o!=0):
    i=i-o
    print "n",i
    x=x+o+1
    if(x>n):
        x=x-n
    print "x",x
    o=x%k
    print "o",o
print i
