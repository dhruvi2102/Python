'''for i in "Python":
    print(i)'''

'''for i in range(1,11):
    print(i) '''

'''for i in range(2,21,2):
    print(i)'''

'''for i in range(1,21,2):
    print(i) '''   

'''for i in range(10,0,-1):
    print(i)  '''  

'''a=int(input("Enter no. : "))

for i in range(1,a+1):
    print(i)'''

'''a=int(input("Enter no. : "))
sum=0

for i in range(1,a+1):
    sum=sum+i
print("Sum = ",sum)'''

a=int(input("Enter no. : "))
evensum=0
oddsum=0

for i in range(1,a+1):
    if i%2==0:
        evensum=evensum+i
    else:
        oddsum=oddsum+i    
print("evensum = ",evensum)
print("oddsum= ",oddsum)
