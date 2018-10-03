class student:
    l1=[]
    def add(self):
        self.l2=[]
        self.l1=[]
        while(1):
            self.nm=raw_input("Enter the name of student :")
            self.rollno=input("Enter the roll number of student :")
            self.l2.append(self.nm)
            self.l2.append(self.rollno)
            self.l1.extend([self.l2])
            self.l2=[] 
            ch=raw_input("Do you want to enter more data. Type y for yes and anything else for no :")
            if(ch.upper() == "Y"):
                continue
            else:
                break

    def read(self):
        print(self.l1)
        for i in self.l1:
            print("Name is ",i[0])
            print("Roll number is ",i[1])

    def delete(self):
        self.rollno=input("Enter the roll number whose record you want to delete :")
        c=-1
        l=self.l1
        print(l)
        for i in self.l1:
            c+=1
            print(c)
            if (self.rollno == i[1]):
                l.pop(c)
                print(l)
            else:
                print("Record does not exist.")
        self.l1=l
        print(self.l1)
    
    def modify(self):
        self.rollno=input("Enter the roll number whose record you want to modify :")
        l=[]
        for i in self.l1:
            if (self.rollno == i[1]):
                l2=[]
                self.nm=raw_input("Enter the modified name :")
                l2.append(self.nm)
                l2.append(self.rollno)
                l.extend([self.l2])
            else:
                print("Record does not exist.")
        self.l1=l
import pickle
file1=open("Test1.dat","wb")
n=input("Enter the number of classes :")
objl=[]
for i in range(n):
    obj=student()
    obj.add()
    objl.append(obj)
    

pickle.dump(objl,file1)
file1.close()
file1=open("Test1.dat","rb")
objl=pickle.load(file1)
for j in objl:
    j.read()
file1.close()
file1=open("Test1.dat","rb+")
objl=pickle.load(file1)
for j in objl:
    j.delete()
file1.close()
file1=open("Test1.dat","rb")
objl=pickle.load(file1)
for j in objl:
    j.read()
file1.close()
