student_name= input("What is your name: ")
course_work_mark= int(input("Enter course work mark: "))
exam_score= int(input("Enter exam score: "))

#score conversion

exam_score_coversion=(exam_score/100)*70
final_mark= (int(exam_score_coversion)+ course_work_mark)

#saving output to file

file= open("final score.txt","w+")
file.write(str(final_mark))

print(f"Hello {student_name} your final score is {final_mark}")