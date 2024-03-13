num=int(input("Enter the last Natural number : "))
a=num+1
sum = 0
print("The sum of the ",num," Natural number is : ")
for i in range(1,a,1) :
    sum+=i
    print(sum)