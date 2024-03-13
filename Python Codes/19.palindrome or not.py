n=int(input("Enter your charactor or number : "))
rev=0
temp=n
while n!=0:
    rem=n%10
    n=n//10
    rev=rev*10+rem
if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")