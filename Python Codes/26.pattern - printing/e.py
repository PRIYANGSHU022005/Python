num = int(input("Enter the value : "))
n = num
for i in range(n,0,-1):
    for j in range(0,n-i,1):
        print(" ",end=" ")
    for k in range(0,i,1):
        print("*",end=" ")
    print()