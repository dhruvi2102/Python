a=input("Enter a : ")
if a[:3]!="ing":
    print(a+'ing')
elif a[:3]=="ing":
    print(a.replace("ing","ly"))    
elif a[0:3]:
    print(a)
else:
    print("done")
