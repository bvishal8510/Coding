num = int(input("Enter the no. of processes  :"))
l=[]
l1=[]
t_a_time=0
for i in range(num):
    l1.append(int(input("Enter arrival time  :")))
    t_a_time += l1[0]
    l1.append(int(input("Enter priority  :")))
    l1.append(int(input("Enter burst time  :")))
    l.extend([l1])
    l1=[]
l=sorted(l)
w_time=0
tat=0
a_w_time=0
a_tat=0

for i in range(len(l)):
    if(i==0):
        w_time += 0
        tat += l[i][2]
    else:
        j=i
        while((l[i-1][2] >= l[j][0]) and (j<(len(l)-1))):
            l[j][0]=i
            j+=1
        l = sorted(l)
        w_time += l[i-1][2]
        tat += l[i][2]
    a_w_time += w_time
    a_tat += tat

print("Average waiting time = ",((a_w_time-t_a_time)/num))
print("Average turn around time = ",((a_tat-t_a_time)/num))