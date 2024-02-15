gender=input("Enter your gender: ")
cgpa = float(input("Entre your CGPA: "))
award="none"

cgpa_class ="None"

if cgpa <= 1.9:
    cgpa_class = "fail"
elif cgpa <= 2.4:
    cgpa_class = "Pass"
elif cgpa <= 3.5:
    cgpa_class="Second Lower"
elif cgpa <= 4.4:
    cgpa_class="Second upper"
elif cgpa <= 5.0:
    cgpa_class = "First class"
    
    if gender =="male":
        award = "Gold medal"
    elif gender == "female":
        award = "Gold medal and a laptop"
    else:
        print("Wrong Gender!!!")

else:
    print("Not a valid CGPA value")

print(f"\nCGPA: {cgpa}\tClass: {cgpa_class}\n")
print(f"You have won {award}")