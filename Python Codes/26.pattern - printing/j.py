num = int(input("Enter the value: "))
n = num + 1
for i in range(1,n,1):
    for j in range(1, i+1,1):
        print(i, end=" ")
    print()
