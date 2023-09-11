a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

if a==b==c:
    print("triangle is equilateral triangle")
if a==b!=c :
    print("triangle is isoceles")
elif a!=b==c:
    print("triangle is isoceles")    
if a!=b!=c:
    print("triangle is scalene")        