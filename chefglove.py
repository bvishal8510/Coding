t = int(input())

def check1(l5,l6):
    for i in range(len(l5)):
        if(l5[i] <= l6[i]):
            pass
        else:
            return 0
    else:
        return 1

def check2(l5,l6):
    for i in range(len(l5)):
        if(l5[i] <= l6[len(l6)-i-1]):
            pass
        else:
            return 0
    else:
        return 1


for i in range(t):
    n = int(input())
    cf = input()
    gf = input()
    gf.rstrip()
    gf.lstrip()
    cf.rstrip()
    cf.lstrip()
    l1=cf.split()
    l2=gf.split()
    l3=[]
    l4=[]
    for i in range(len(l1)):
        l3.append(int(l1[i]))
        l4.append(int(l2[i]))
    if((len(l3) == n) and (len(l4)==n)):
        if((cf == gf) and (cf == gf[::-1])):
            print("both")
        elif(check1(l3,l4)):
            print("front")
        elif(check2(l3,l4)):
            print("back")
        else:
            print("none")
    else:
        print("none")