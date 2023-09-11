myset={'A','B','C','Y','U','O'}
print(myset)

#print(myset[0]) index not supported

if 'C' in myset:
    print("Yes...")
else:
    print("No...")    

for i in myset:
    print(i)    

#---------------------Inbuilt Methods--------------------
# myset.add('P') 
# myset.update(['X','I','L'])
# myset.remove('A')

# myset.clear()
# del myset   

newset={'A','B','I','R','W','Q'}

#x=myset.union(newset) 
x=myset.intersection(newset)
print(x)
