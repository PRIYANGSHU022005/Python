n = int(input("Enter the num = "))
num = n+1
f = 1

if (n < 0):
    print("Factorial is not defined for negative numbers.")
elif (n == 0):
    print("The factorial of 0 is 1")
else:
    print("The all stages of Factorial are = ")
    for i in range(1, num, 1):
        f *= i
        print(f,end=" , ")
    print()
    print("Factorial of", n, "is ",f)