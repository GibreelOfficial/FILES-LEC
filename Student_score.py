student_name= input("What is your name: ")
course_work_mark= int(input("Enter course work mark: "))
exam_score= input("Enter exam score: ")

score_coversion=(course_work_mark/100)*70

file= open("course work score.txt","w+")
file.write(str(score_coversion))
file.write(exam_score)

print(f"Hello,{student_name} your course work score is {score_coversion}")