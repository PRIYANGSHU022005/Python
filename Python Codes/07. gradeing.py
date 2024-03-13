user=int(input("Enter the Mark here :"))
if (user >= 90 and user < 101) :
    print("The grade is Outstanding or O .")
elif(user >= 80 and user < 90) :
    print("The grade is A .")
elif(user >= 70 and user < 80) :
    print("The grade is B .")
elif(user >= 60 and user < 70) :
    print("The grade is C .")
elif(user >= 45 and user < 60) :
    print("The grade is D .")
elif(user >= 25 and user < 45) :
    print("The grade is E .")
elif(user >= 0 and user < 25) :
    print("The grade is F or You are Fail .")
else :
    print("Wrong Choice !!")

