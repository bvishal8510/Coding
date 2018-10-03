print "Enter 1. to insert element at beginning."
print "Enter 2. to insert element at end."
print "Enter 3. to insert element at desired position."
print "Enter 4. to delete element from beginning."
print "Enter 5. to delete last element."
print "Enter 6. to delete element from desired position."
print "Enter 7. to display list contents."
print "Enter 8. to quit."

l=[]
while(1):
    print"\n"*1
    ch=input("Enter your choice.")
    if(ch==1):
        el=input("Enter the element to be inserted :")
        l.insert(0,el)
        
    elif(ch==2):
        el=input("Enter the element to be inserted :")
        l.append(el)
        
    elif(ch==3):
        el=input("Enter the element to be inserted :")
        print "Your list is ",l
        po=input("Enter the position where you want to enter the element :")
        if(po>len(l)):
            print "Your index is out of range."
        else:
            l.insert((po-1),el)
            
    elif(ch==4):
        if(l==[]):
            print "List is empty."
        else:
            l.pop(0)
            
    elif(ch==5):
        if(l==[]):
            print "List is empty."
        else:
            l.pop(-1)
            
    elif(ch==6):
        if(l==[]):
            print "List is empty."
        else:
            print "Your list is ",l
            po=input("Enter the position from where you want to delete the element :")
            if(po>len(l)):
                print "Index number does not exist."
            else:
                l.pop(po-1)
    elif(ch==7):
        print "List contents are ",l
    elif(ch==8):
        break
    else:
        print "Invalid choice.Please reenter your chioce"
