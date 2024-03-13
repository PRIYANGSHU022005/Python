num = int(input("Enter the value: "))
n = num
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print(i, end=" ")
    print()
