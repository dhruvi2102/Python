a=input("Enter a : ")
b=input("Enter b : ")

x=a+b

start = x[0]
end=x[-1]

swap=end+x[1:-1]+start

print(swap)
