Stack = []
Size = 5
def Display():
 print("Stack contains:")
 for x in Stack:
  print(x)
def Push(n):
 if len(Stack) < Size:
  Stack.append(n)
 else:
  print("Stack is full")
def Pop():
 if len(Stack) > 0:
  Stack.pop()
 else:
  print("Stack is empty.")
