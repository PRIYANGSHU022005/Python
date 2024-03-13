num=int(input("Enter the first Natural number : "))
num1=int(input("Enter the last Natural number : "))
a=num1+1
sum = 0
print("The sum of the ",num1," Natural number is : ")
for i in range(num,a,1) :
    sum+=i
    print(sum)