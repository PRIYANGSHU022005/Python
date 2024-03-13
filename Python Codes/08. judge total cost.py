unit=int(input("enter the quantity"))
p=unit*1
if (p>999):
    print("we provide 20% discount each 1000 purchase")
    p=p-p*(10 / 100)
    print('you need to pay rs',p)
else:
    print("we can't provide any discount !!")
    print("you need to pay rs.",p)