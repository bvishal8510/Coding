num = int(input("Enter the no. of processes  :"))
l=[]
l1=[]
d={}
t_a_time=0
for i in range(num):
    d[i]=0
    l1.append(int(input("Enter arrival time  :")))
    t_a_time += l1[0]
    l1.append(int(input("Enter burst time  :")))
    l.extend([l1])
    l1=[]
l=sorted(l)
q = int(input("Enter time quanta  :"))
time=0
a_w_time=0
a_tat=0
i=-1

def check(l):
    for i in range(len(l)):
        if(l[i][1] > 0):
            return 0
    else:
        return 1         

while(1):
    i=((i+1)%num)
    print("i = ",i)
    # print(check(l))
    if(check(l)):
        break
    else:
        time += q
        if(((l[i][1]-q)<1) and ((l[i][1]-q)>(-num))):
            a_w_time += (time - d[i])
            a_tat += (time + l[i][1] - d[i])
            l[i][1] -= q
    
        elif((l[i][1]-q) > 0):
            l[i][1] -= q
            d[i]= d[i]+q

    print("T =",time)
    print("l =",l)
    

print("Average waiting time = ",((a_w_time-t_a_time)/num))
print("Average turn around time = ",((a_tat-t_a_time)/num))