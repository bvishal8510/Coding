t=input()
for i in range(t):
    ct=0
    ca=0
    l=[]
    ln=[]
    
    n=input()
    s=raw_input()
    l=s.split(" ")
    for i in range(len(l)):
        ln.append(int(l[i]))
    c=1
    for i in range(len(ln)):
        c=c+1
        if(c%2==0):
            if(ln[i]%2!=0):
                ln[i]=ln[i]-1
                if(ca<0):
                    ct=ct+1
                ca=ca+1
            print "ct1",ct
            print "ca1",ca
        elif(c%2!=0):
            if(ln[i]%2==0):
                ln[i]=ln[i]+1
                if(ca>0):
                    ct=ct+1
                ca=ca-1
            print "ca1",ca
            print "ct2",ct
        print ln
    print ct
    
        
    
