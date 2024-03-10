a=int(input("Enter the starting range : "))
b=int(input("Enter the ending range : "))
if(a%2==0 and b%2==0):
    for i in range(a,b+1,2):
        print("The Even range is :",i)
elif(a%2==0 and b%2!=0):
    b1 = b + 2
    for k in range(a,b1-1,2):
        print("The Even range is :",k)
elif(a%2!=0 and b%2==0):
    b1=b+2
    for l in range(a+1,b1,2):
        print("The Even range is :",l)
else:
    for j in range(a,b,2):
        print("The Even range is :",j+1)
