mytup=('Rajkot','Ahmedabad','Surat','Bhavnagar')
print(mytup)

print(mytup[0])
print(mytup[2:4])
print(mytup[0::2])
print(len(mytup))

if 'Rajkot' in mytup:
    print("Yes..")
else:
    print("no...")

for items in mytup:
    print(items)        

print(mytup.count('Surat'))   
print(mytup.index('Ahmedabad'))

del mytup
print(mytup)