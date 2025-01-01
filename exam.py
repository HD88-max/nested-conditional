medical_cause = input("Do you have a medical cause - Y for yes and N for no: ")

attendance = int(input("What is your attendance % ? "))

if medical_cause == "Y":
    print("You are allowed in the exam.")
else:
    if attendance > 75:
        print("You are allowed")
    else:
        print("You are not able to attend this exam.")    