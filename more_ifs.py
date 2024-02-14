birth_year=int(input("Your birth year: "))
current_year=2024

age=(current_year-birth_year)

print(f"Your age is {age}\n")

if age >= 0 and age <= 3:
    print("This a baby")
elif age <= 10:
    print("This is a kid")
elif age <= 20:
    print("This is a teenager")
elif age <= 35:
    print("This is a youth")
elif age <= 50:
    print("This is a Senior citizen")
elif age >50:
    print("This is an elder")
    
print("Thank you!")