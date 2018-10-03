num = int(input("Enter the no. of processes  :"))
l=[]

for i in range(num):
    l.append(int(input("Enter burst time  :")))

w_time=0
tat=0
a_w_time=0
a_tat=0

for i in range(len(l)):
    if(i==0):
        w_time += 0
        tat += l[i]
    else:
        w_time += l[i-1]
        tat += l[i]
    
    a_w_time += w_time
    a_tat += tat

print("Average waiting time = ",(a_w_time/num))
print("Average turn around time = ",(a_tat/num))