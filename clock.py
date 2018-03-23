n = input()
if('PM' in n):
    n1 = int(n[0]+n[1])
    n1 = n1 +12
    print(str(n1)+n[2:8])
else:
    n1 = int(n[0]+n[1])
    print('1',n1)
    if(n1 == 12):
        print('00'+n[2:8])
    else:
        print(n[0:8])