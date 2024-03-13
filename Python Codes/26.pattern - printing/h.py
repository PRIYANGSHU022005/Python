num = int(input("Enter the value: "))
n = num + 1
count = 1
for i in range(1, n):
    for j in range(1, i + 1):
        print(count, end=" ")
        count += 1
    print()
