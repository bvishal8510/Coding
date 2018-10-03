Stack = []
def Display():
    if Stack == []:
        print("Stack is empty")
    else:
        print("Stack contains:")
        for x in Stack:
            print(x)

def Push():
    n=int(input("Enter number"))
    Stack.append(n)

def Pop():
    if Stack == []:
        print("Stack is empty.")  
    else:
        Stack.pop()
  

print("Enter 1 to push element .")
print("Enter 2 to pop element .")
print("Enter 3 to display element .")
print("Enter 4 to quit .")
while(1):
    print()
    ch=int(input("Enter your choice :"))
    if (ch==1):
        Push()
    elif (ch==2):
        Pop()
    elif (ch==3):
        Display()
    elif(ch==4):
        break
    else:
        print("Wrong input. Please re-enter")
