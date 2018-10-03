f1=open("f1.txt","w")
# sen = ["I am a good boy.\n","He used tot play with me.\n","he is very good."]
sen = input("Enter sentence   :  ")
f1.writelines(sen)
f1.close()
f1=open("f1.txt","r")
l=f1.readlines()
print("Contents of file")
for i in l:
    print(i)