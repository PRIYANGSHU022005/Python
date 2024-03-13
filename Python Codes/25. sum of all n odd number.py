num = int(input("Enter the number: "))
n = num * 2
sumEvenNum = 0
for i in range(1,n,2):
    sumEvenNum += i
print("Sum of the first", num, "odd natural numbers:", sumEvenNum)
