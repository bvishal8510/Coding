class student1(object):
    def __init__(self,rno):
        self.rno = rno
    def printdata1(self):
        print("The roll no. is  = ",self.rno)
        
class student2(student1):
    def __init__(self,age,rno):
        student1.__init__(self,rno)
        self.age = age
    def printdata2(self):
        print("The age is  = ",self.age)
        
class derived(student2):
    def __init__(self,name,rno,age):
        self.name = name
        student2.__init__(self,age,rno)
    def printdata3(self):
        print("The name is  = ",self.name)
        derived.printdata1(self)
        derived.printdata2(self)
        
obj = derived("Vishal",730,16)
obj.printdata3()
