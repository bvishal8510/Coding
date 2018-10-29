class student(object):
    def __init__(sel,rno):
        sel.rno=rno
    def printdata1(sel):
        print("The roll no. is =",sel.rno)

class derived(student):
    def __init__(sel,name,rno):
        sel.name=name
        student.__init__(sel,rno)
    def printdata2(sel):
        print("The name is =",sel.name)
obj=derived("Vishal",730)
obj.printdata1()
obj.printdata2()
