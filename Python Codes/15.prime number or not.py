num=int(input("Enter the number : "))
flag = 0
if num>1:
    for i in range(2,int(num//2)+1,1):
        if(num % i == 0):
            flag = 1
            break
else:
    print("",num," is not a non applicable .")
if(flag == 0):
    print("",num," is a Prime number .")
else:
    print("",num," is not a Prime number .")