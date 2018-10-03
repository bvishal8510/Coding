class student(object):
    def __init__(sel,name,rno):
        sel.rno=rno
        sel.name=name
        print("Constructor is automtically called")
    def printdata1(sel):
        print("The roll no. is =",sel.rno)
        print("The name is =",sel.name)

obj=student("Vishal",730)
obj.printdata1()

obj2=student("Yash",480)
obj2.printdata1()
