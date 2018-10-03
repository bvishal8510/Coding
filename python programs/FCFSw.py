num = int(input("Enter the no. of processes  :"))
l=[]
l1=[]
for i in range(num):
    l1.append(int(input("Enter arrival time  :")))
    l1.append(int(input("Enter burst time  :")))
    l.extend([l1])
    l1=[]
l=sorted(l)
w_time=0
tat=0
a_w_time=0
a_tat=0
t_a_time=0

for i in range(len(l)):
    t_a_time += l[i][0]
    if(i==0):
        w_time += 0
        tat += l[i][1]
    else:
        w_time += l[i-1][1]
        tat += l[i][1]
    a_w_time += w_time
    a_tat += tat

print("Average waiting time = ",((a_w_time-t_a_time)/num))
print("Average turn around time = ",((a_tat-t_a_time)/num))