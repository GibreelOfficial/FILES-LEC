classes_attended=int(input("Enter number of classes attended: "))
attendance_percentage=(classes_attended/15)*100

if attendance_percentage>75:
    print(f"You attended {int(attendance_percentage)}% of classes\nYou are eligible to sit for exams")
else:
    medical_condition=input("Do you have a medical cause for under attendance (press Y or N )")
    if medical_condition=="y":
        print("You are eligible to sit for exams")
    else:
        print("You are not eligible to sit for exams")