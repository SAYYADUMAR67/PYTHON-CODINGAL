medical_cause = input("did you have any medical cause? (yes/no): ").strip().upper()



if medical_cause == "YES":
    print("You are allowed to take the exam.")
else:

    attendance = int(input("Enter your attendance percentage: "))
    if attendance >= 75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam.")