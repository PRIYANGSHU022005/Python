a=int(input("A = "))
b=int(input("B = "))
c=int(input("C = "))

if(a>b and a>c):
    print("The number of A is Greater . ")
elif(b>c):
    print("The number of B is Greater . ")
elif(a==b==c):
    print("The number is Equal .")
else:
    print("The number of C is Greater .")
