print("\nPress 1 for Addition .")
print("\nPress 2 for Subtraction .")
print("\nPress 3 for Multiplication .")
print("\nPrint 4 for find Power .")
print("\nPress 5 for Divide .")
print("\nPress 6 for Float Division .")
print("\nPrint 7 for Modulation .")

choice = input("\n\nEnter your choice : ")
# Perform the selected operation
if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
    print("Invalid input. Please choose a valid operation.")
else:
    n1 = float(input("Enter the first number : "))
    n2 = float(input("Enter the second number : "))
    if choice == '1':
        add = n1 + n2
        print("The Addition of ", n1, " & ", n2, " = ", add)
    elif choice == '2':
        sub = n1 - n2
        print("The Subtraction of ", n1, " & ", n2, " = ", sub)
    elif choice == '3':
        multiply = n1 * n2
        print("The Multiplication of ", n1, " & ", n2, " = ", multiply)
    elif choice == '4':
        pow = n1 ** n2
        print("The Power of ", n1, " is = ", pow)
    elif choice == '5':
        div = n1 / n2
        print("The Division of ", n1, " by ", n2, " is = ", div)
    elif choice == '6':
        fd = n1 // n2
        print("The Float Division of ", n1, " by ", n2, " is = ", fd)
    elif choice == '7':
        mod = n1 % n2
        print("The Modulation of ", n1, " by ", n2, " is = ", mod)
