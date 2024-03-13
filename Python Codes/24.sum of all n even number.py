num = int(input("Enter the number : "))
n = num + 1
sumEven = 0
for i in range(1,n,1):
    sumEven += 2 * i
print("Sum of the first", num, "even natural numbers:", sumEven)
