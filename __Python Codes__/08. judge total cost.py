unit=int(input("Enter the quantity : "))
p=unit*100
if p>1000:
    print("We provide 10% discount each 1000 purchase .  ")
    p=p-(p/10)
    print("You need to pay Rs.",p)
else:
    print("We can't provide any discount !!")
    print("You need to pay Rs.",p)