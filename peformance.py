students =["musa", "Mariam", "Peter", "Peace"]
subjects =["Math", "English", "Science", "SST" ]

pass_count =0
fail_count =0

number_of_subjects= students.count()
average_pass_mark = 65

print(number_of_subjects)
for student in students:
    total= int(input(f"{student}'s Total: "))

    student_average =total/number_of_subjects

    if student_average >= average_pass_mark:
        pass_count +=1
    else:
        fail_count +=1
 
print(f"\nTotal passes: {pass_count}\n Total failures: {fail_count}")
