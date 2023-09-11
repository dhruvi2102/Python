"""#IF STATEMENT

marks = int(input("Enter Marks : "))

if marks>75:
    print("You will get a car")

#IF ELSE STATEMENT

marks = int(input("Enter Marks : "))

if marks>75:
    print("You will get a car")
else:
    print("You will get a rickshaw")"""

'''num = int(input("Enter number : "))
if num%2==0:
    print("It is an even number")
else:
    print("It is an odd number")'''

'''name= input("Enter your name : ")
age=int(input("Enter your age : "))
if age>18:
    print("You can vote")
else:
    print("You cannot vote")    '''

'''#ELIF STATEMENT

num =int(input("Enter Number : "))

if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Number is zero")  '''      

#NESTED IF

a=100
b=500

if a==100:
   if b==400:
      print("a is 100 and b is 400")
   else:
      print("nested else")
else:
   print("Main else")        
      