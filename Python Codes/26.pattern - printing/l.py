num = int(input("Enter the value: "))
n = num + 1
for i in range(n,1,-1):
    for j in range(1,i,1):
        print(j, end=" ")
    print()
