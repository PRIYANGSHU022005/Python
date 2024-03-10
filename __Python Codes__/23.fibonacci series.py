num = int(input("Enter the number : "))
fs = []
if(num <= 0) :
    print("Fibonacci Series is not defined for non-positive number . ")
elif(num == 1) :
    fs = [0]
    print("The Fibonacci Series of ",num," number is = ",fs)
else:
    fs = [0,1]
    print("The all stages of Fibonacci Series are = ",end=" ")
    for i in range(2,num,1) :
        next_num = fs[-1] + fs[-2]
        fs += [next_num]
        print(next_num,end=" , ")

    print("\n")
    print("The Fibonacci Series of ",num," number is : ",fs)